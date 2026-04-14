#!/bin/bash
chemprop predict \
  -i data/processed/screening_library_final.csv \
  --model-paths models/finetune_model_v5_scaffold/replicate_*/model_0/best.pt \
  -o results/screening_results_v5.csv \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized