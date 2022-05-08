#!/bin/bash

python utils/Q2/run_Q2.py \
      --infile data/Q2_baselines/dodeca_consistent.csv \
      --gen_method beam \
      --q_per_cand single \
      --personal remove \
      --outfile /home/willy/comp5214-groundedness-kgd/data/Q2_baselines/results/output_dodeca_consistent_T5 \
      --save_steps >> /home/willy/comp5214-groundedness-kgd/data/Q2_baselines/results/output_dodeca_consistent_T5.txt

python utils/Q2/run_Q2.py \
      --infile data/Q2_baselines/dodeca_inconsistent.csv \
      --gen_method beam \
      --q_per_cand single \
      --personal remove \
      --outfile /home/willy/comp5214-groundedness-kgd/data/Q2_baselines/results/output_dodeca_inconsistent_T5 \
      --save_steps >> /home/willy/comp5214-groundedness-kgd/data/Q2_baselines/results/output_dodeca_inconsistent_T5.txt

python utils/Q2/run_Q2.py \
      --infile data/Q2_run/Q2_0_shot.csv \
      --gen_method beam \
      --q_per_cand single \
      --personal remove \
      --outfile /home/willy/comp5214-groundedness-kgd/data/Q2_run/Q2_0_shot_out \
      --save_steps >> /home/willy/comp5214-groundedness-kgd/data/Q2_run/output_0_shot.txt

python utils/Q2/run_Q2.py \
      --infile data/Q2_run/Q2_1_shot.csv \
      --gen_method beam \
      --q_per_cand single \
      --personal remove \
      --outfile /home/willy/comp5214-groundedness-kgd/data/Q2_run/Q2_1_shot_out \
      --save_steps >> /home/willy/comp5214-groundedness-kgd/data/Q2_run/output_1_shot.txt

python utils/Q2/run_Q2.py \
      --infile data/Q2_run/Q2_2_shot.csv \
      --gen_method beam \
      --q_per_cand single \
      --personal remove \
      --outfile /home/willy/comp5214-groundedness-kgd/data/Q2_run/Q2_2_shot_out \
      --save_steps >> /home/willy/comp5214-groundedness-kgd/data/Q2_run/output_2_shot.txt
