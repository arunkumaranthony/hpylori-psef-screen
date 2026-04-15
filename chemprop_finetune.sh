#!/bin/bash
chemprop train \
  --data-path data/processed/fine_tune_ext.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --checkpoint models/pretrain_v6_base/model_0/best.pt \
  --save-dir models/finetune_v6_base_scaffold \
  --epochs 50 \
  --class-balance \
  --split scaffold_balanced \
  --num-replicates 10