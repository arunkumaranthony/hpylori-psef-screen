#!/bin/bash
# Runs optimization using random search to prevent memory overflows

chemprop hpopt \
  --data-path data/processed/fine_tune.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary v1_rdkit_2d_normalized \
  --split scaffold_balanced \
  --raytune-search-algorithm random \
  --raytune-num-samples 50 \
  --output-dir models/hpopt_temp \
  --hpopt-save-dir models/hpopt_results