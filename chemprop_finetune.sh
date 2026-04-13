chemprop train \
  --data-path data/processed/fine_tune.csv \
  --task-type classification \
  --smiles-columns smiles \
  --target-columns activity \
  --molecule-featurizers morgan_binary \
  --checkpoint models/pretrain_model_v2/model_0/best.pt \
  --save-dir models/finetune_model_v2 \
  --epochs 50 \
  --class-balance