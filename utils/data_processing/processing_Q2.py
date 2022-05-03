import csv
import argparse
from datasets import load_dataset


def process_q2_csv(wow, prompt, save_path, args):
    fieldnames = ["episode_idx", "round", "topic", "message", "response", "knowledge", "gold"]
    rows = []

    
        cur_data["episode_idx"] = episode_idx
        cur_data["round"] = round
        cur_data["topic"] = topic       
        cur_data["message"] = message
        cur_data["response"] = response
        cur_data["knowledge"] = knowledge
        cur_data["gold"] = gold
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
    save_path = "/home/willy/comp5214-groundedness-kgd/data/Q2_run/quac_processed.csv"
    wow_path = "/home/willy/comp5214-groundedness-kgd/data/wizard_of_wikipedia/test_topic_split.json"
    process_q2_csv(quac, save_path, args)