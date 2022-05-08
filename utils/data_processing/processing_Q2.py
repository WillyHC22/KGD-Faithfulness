import csv
import argparse
import pandas as pd
from datasets import load_dataset


def process_q2_csv(processed_prompt_path, generated_path, save_path):
    fieldnames = ["episode_idx", "topic", "round", "message", "response", "knowledge", "gold"]
    rows = []
    episode_idx = 0

    processed_prompt = pd.read_csv(processed_prompt_path)
    generated = pd.read_csv(generated_path)

    for index in range(len(processed_prompt)):
        cur_data = {}

        output = generated.iloc[index]["output"]
        if output[-4:] == "</s>":
            response = output[6:-4]
        else:
            response = output[6:]

        cur_data["episode_idx"] = episode_idx
        cur_data["round"] = processed_prompt.iloc[index]["round_nb"]
        cur_data["topic"] = processed_prompt.iloc[index]["topic"]
        cur_data["message"] = processed_prompt.iloc[index]["message"][13:]
        cur_data["response"] = response
        cur_data["knowledge"] = processed_prompt.iloc[index]["knowledge"]
        cur_data["gold"] = processed_prompt.iloc[index]["gold"][9:]
        rows.append(cur_data)

        episode_idx += 1

    with open(save_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--kshot", required=True, type=int, help="which few shot you want to process: 0/1/2 for now")
    parser.add_argument("--save_file", default="Q2", type=str, help="Name the output file")
    args = parser.parse_args()

    kshot = args.kshot
    save_file = args.save_file
    save_path = f"/home/willy/comp5214-groundedness-kgd/data/Q2_run/{save_file}_{kshot}_shot.csv"
    processed_prompt_path = f"/home/willy/comp5214-groundedness-kgd/data/processed_prompt/prompts_{kshot}_shot.csv"
    generated_path = f"/home/willy/comp5214-groundedness-kgd/data/generated_data/output_{kshot}_shot.csv"
    process_q2_csv(processed_prompt_path, generated_path, save_path)