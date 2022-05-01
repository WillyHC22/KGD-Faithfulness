import re
import torch
import json
import csv
# from tqdm import tqdm
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from datasets import load_dataset

def process_wow_csv(wow, save_path):
    fieldnames = ["index", "dialogue", "knowledge", "speakers", "number_of_turns", "word_count"]
    rows = []
    index = 0
    word_count = 0
    for data in wow: #968 conversations
        cur_data = {}
        dialogue = []
        speakers = []
        dialog = data["dialog"]
        knowledge = data["chosen_topic_passage"]
        number_of_turns = len(knowledge)

        for i in range(len(dialog)):
            text = dialog[i]["text"]
            speaker = dialog[i]["speaker"][2:]
            #dialog_turn = f" {speaker}: {text}"
            dialog_turn = " " + speaker + ": " + text
            word_count += len(dialog_turn.split())

            dialogue.append(dialog_turn)
            speakers.append(speaker)

        cur_data["word_count"] = word_count
        cur_data["number_of_turns"] = number_of_turns
        cur_data["speakers"] = speakers       
        cur_data["dialogue"] = dialogue
        cur_data["knowledge"] = knowledge
        cur_data["index"] = index
        rows.append(cur_data)
        index += 1
    
    with open(save_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    wow_path = "/home/willy/comp5214-groundedness-kgd/data/wizard_of_wikipedia/test_topic_split.json"
    save_path = "/home/willy/comp5214-groundedness-kgd/data/wizard_of_wikipedia/wow_processed.csv"
    with open(wow_path, "r") as f:
        wow = json.loads(f.read())

    process_wow_csv(wow, save_path)