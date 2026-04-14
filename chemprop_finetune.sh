#!/bin/bash
chemprop train \
  --data-path data/processed/fine_tune.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized \
  --checkpoint models/pretrain_model_v4/model_0/best.pt \
  --save-dir models/finetune_model_v5_scaffold \
  --epochs 50 \
  --class-balance \
  --split scaffold_balanced \
  --num-replicates 10