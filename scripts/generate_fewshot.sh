#!/bin/bash

python src/generate.py \
      --save_file output \
      --kshot 0

python src/generate.py \
      --save_file output \
      --kshot 1

python src/generate.py \
      --save_file output \
      --kshot 2