import json
import csv
import ast
import numpy as np
import pandas as pd 
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def get_dialogue(row_wow):
    final_dialogue = ""
    speakers = ast.literal_eval(row_wow["speakers"])
    dialogue_turns = ast.literal_eval(row_wow["dialogue"])
    knowledge_turns = ast.literal_eval(row_wow["knowledge"])

    if speakers[3] == "Wizard": #We want to infer on wizard conversation because we have the knowledge they use
        dialogue = dialogue_turns[:3]
        knowledge = knowledge_turns[2]
    else:
        dialogue = dialogue_turns[:4]
        knowledge = knowledge_turns[3]
    dialogue = " ".join(dialogue)

    final_dialogue += f"Given the knowledge and the conversation, write the next turn of the conversation. Knowledge: {knowledge} Conversation: {dialogue}"

    return final_dialogue


def craft_prompt(quac, wow, save_path_csv, kshot=2):

    fieldnames = ["index", "topic", "prompt"]
    rows = []

    for global_index, row_wow in wow.iterrows():
        cur_data = {}
        prompt = ""
        indexes = quac.sample(kshot).index
        topic = row_wow["topic"]

        if row_wow["number_of_turns"] < 5: #Should be moved to wow_processing, quickfix for now
            continue

        for index in indexes:
            cur_row = quac.iloc[index]

            ans_questions = ast.literal_eval(cur_row["ans_questions"])
            ans_answers = ast.literal_eval(cur_row["ans_answers"])
            ans_starts = ast.literal_eval(cur_row["ans_start"])


            context = cur_row["context"][:(ans_starts[-1]+len(ans_answers[-1])+10)] #cut context
            prompt += f"Context: {context} "

            unans_question = cur_row["unans_questions"]
            prompt += f"Question: {unans_question} Answer: None. "

            for question, answer in zip(ans_questions, ans_answers):
                prompt += f"Question: {question} Answer: {answer} "
            
        dialogue_turn = get_dialogue(row_wow)
        prompt += dialogue_turn
        quac.drop(quac.index[indexes], inplace=True)
        quac.reset_index(drop=True, inplace=True)
        cur_data["index"] = global_index
        cur_data["prompt"] = prompt
        cur_data["topic"] = topic
        rows.append(cur_data)

    with open(save_path_csv, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    np.random.seed(42)

    #tokenizer = AutoTokenizer.from_pretrained("bigscience/T0_3B")
    #model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0_3B")
    kshot = 2
    save_path_csv = f"/home/willy/comp5214-groundedness-kgd/data/processed_prompt/prompts_{kshot}_shot.csv"
    quac = pd.read_csv("/home/willy/comp5214-groundedness-kgd/data/QuAC/quac_processed.csv")
    wow = pd.read_csv("/home/willy/comp5214-groundedness-kgd/data/wizard_of_wikipedia/wow_processed.csv")

    craft_prompt(quac, wow, save_path_csv, kshot=kshot)