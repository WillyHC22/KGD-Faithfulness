#!/bin/bash

python run_Q2.py \
      --infile /data/Q2_run/Q2_0_shot.csv \
      --gen_method beam \
      --q_per_cand single \
      --personal remove \
      --outfile /home/willy/comp5214-groundedness-kgd/data/Q2_run/Q2_0_shot_out \
      --save_steps >> /home/willy/comp5214-groundedness-kgd/data/Q2_run/output_0_shot.txt
