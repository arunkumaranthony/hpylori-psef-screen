#!/bin/bash
# Screens the Broad Institute library using the 10-model consensus

chemprop predict \
  -i data/processed/screening_library_final.csv \
  --model-paths models/finetune_model_v4/model_*/best.pt \
  -o results/screening_results_v4.csv \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized