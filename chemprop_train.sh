#!/bin/bash
chemprop train \
  --data-path data/processed/pre_train_ext.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --save-dir models/pretrain_v6_base \
  --epochs 20