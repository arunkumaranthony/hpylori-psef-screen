#!/bin/bash
chemprop train \
  --data-path data/processed/pre_train_ext.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized \
  --save-dir models/pretrain_model_ext \
  --epochs 20