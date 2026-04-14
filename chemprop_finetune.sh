#!/bin/bash
# Fine-tunes the foundation model into a 10-model ensemble for H. pylori

chemprop train \
  --data-path data/processed/fine_tune.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized \
  --checkpoint models/pretrain_model_v4/model_0/best.pt \
  --save-dir models/finetune_model_v4 \
  --epochs 50 \
  --class-balance \
  --ensemble-size 10