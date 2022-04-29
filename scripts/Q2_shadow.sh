#!/bin/bash

# python run_Q2.py \
#       --infile /data/dodeca_consistent.csv \
#       --gen_method beam \
#       --q_per_cand single \
#       --personal remove \
#       --outfile /home/willy/comp5214-groundedness-kgd/data/dodeca_consistent_out \
#       --save_steps >> /home/willy/comp5214-groundedness-kgd/data/output_consistent.txt

python Q2/run_Q2.py \
      --infile data/dodeca_consistent.csv \
      --gen_method beam \
      --q_per_cand single \
      --personal remove \
      --outfile /home/shadowtungtung/comp5214/comp5214-groundedness-kgd/data/dodeca_consistent_out \
      # --save_steps >> /home/shadowtungtung/comp5214/comp5214-groundedness-kgd/data/output_consistent.txt