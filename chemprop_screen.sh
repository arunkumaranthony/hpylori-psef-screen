#!/bin/bash
chemprop predict \
  --test-path data/processed/screening_library_final.csv \
  --model-path models/finetune_v6_rdkit_scaffold/replicate_*/model_0/best.pt \
  --preds-path results/v6_screening_predictions.csv \
  --smiles-columns smiles \
  --molecule-featurizers v1_rdkit_2d_normalized