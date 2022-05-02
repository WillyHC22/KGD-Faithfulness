import csv
import argparse
from datasets import load_dataset


def process_quac_csv(quac, save_path, args):
    fieldnames = ["dialogue_id", "context", "ans_questions", "ans_answers", "ans_start", "unans_questions", "unans_answers"]
    rows = []
    for data in quac:
        cur_data = {}
        context = data["context"]
        dialogue_id = data["dialogue_id"]

        #If no unanswerable question, skip this sample
        answers = [answer[0] for answer in data["answers"]["texts"]]
        if "CANNOTANSWER" not in answers:
            continue
        #If the two answerable questions have answers that have start_answer > 600, skip this sample
        answer_starts = [answer_start[0] for answer_start in data["answers"]["answer_starts"][:2]] #debug here to get two minimums
        if answer_starts[-1] > args.max_answer_starts:
            continue
        if answer_starts[0] > args.max_answer_starts:
            continue

        unans_index = answers.index("CANNOTANSWER")
        unans_question = data["questions"][unans_index]
        unans_answer = None

        ans_questions = [question for question in data["questions"][:2]]
        ans_answers = [answer[0] for answer in data["answers"]["texts"][:2]]

        cur_data["dialogue_id"] = dialogue_id
        cur_data["context"] = context
        cur_data["ans_questions"] = ans_questions       
        cur_data["ans_answers"] = ans_answers
        cur_data["ans_start"] = answer_starts
        cur_data["unans_questions"] = unans_question
        cur_data["unans_answers"] = unans_answer
        rows.append(cur_data)

    
    with open(save_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--max_answer_starts", type=int, required=False, default=400, help="max index for the answers (so we can cut the context until the highest anser_start)")
    args = parser.parse_args()

    quac = load_dataset("quac", split="train")
    save_path = "/home/willy/comp5214-groundedness-kgd/data/QuAC/quac_processed.csv"

    process_quac_csv(quac, save_path, args)