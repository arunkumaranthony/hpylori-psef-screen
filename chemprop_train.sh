chemprop train \
  --data-path data/processed/pre_train.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary \
  --save-dir models/pretrain_model_v2 \
  --epochs 20