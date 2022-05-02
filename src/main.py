import json
import csv
import ast
import numpy as np
import pandas as pd 
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def main(prompts, save_path_csv):
    tokenizer = AutoTokenizer.from_pretrained("bigscience/T0_3B")
    model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0_3B")

    fieldnames = ["prompt", "output"]
    rows = []
    for index, row in tqdm(prompts.iterrows()):
        cur_data = {}
        prompt = row["prompt"]
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(inputs)

        cur_data["prompt"] = prompt
        cur_data["output"] = output
        rows.append(cur_data)

    with open(save_path_csv, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    kshot = 1
    save_path_csv = "/home/willy/comp5214-groundedness-kgd/data/generated_data/output.csv"
    prompts = pd.read_csv(f"/home/willy/comp5214-groundedness-kgd/data/processed_prompt/prompts_{kshot}_shot.csv")
    main(prompts, save_path_csv)