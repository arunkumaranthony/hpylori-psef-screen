chemprop predict \
  -i data/processed/screening_library_final.csv \
  --model-paths models/finetune_model_v2/model_0/best.pt \
  -o results/screening_results_v2.csv \
  --molecule-featurizers morgan_binary