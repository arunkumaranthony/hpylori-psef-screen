#!/bin/bash
# Pre-trains the foundation model on the large, general ChEMBL dataset

chemprop train \
  --data-path data/processed/pre_train.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized \
  --save-dir models/pretrain_model_v4 \
  --epochs 20