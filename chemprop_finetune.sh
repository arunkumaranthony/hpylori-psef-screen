#!/bin/bash
chemprop train \
  --data-path data/processed/fine_tune_ext.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized \
  --checkpoint models/pretrain_model_ext/model_0/best.pt \
  --save-dir models/finetune_model_ext_scaffold \
  --epochs 50 \
  --class-balance \
  --split scaffold_balanced \
  --num-replicates 10