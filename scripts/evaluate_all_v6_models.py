import pandas as pd
import numpy as np
import glob
from sklearn.metrics import roc_auc_score, average_precision_score

# 1. Load the exact answers and rename the column so it doesn't clash
df_truth = pd.read_csv("data/processed/fine_tune_ext.csv")
df_truth = df_truth[['smiles', 'activity']].rename(columns={'activity': 'true_activity'})

experiments = {
    "1. Train from Scratch (No Pretrain)": "models/finetune_v6_scratch_scaffold/replicate_*/model_0/test_predictions.csv",
    "2. Base MPNN (No RDKit)": "models/finetune_v6_base_scaffold/replicate_*/model_0/test_predictions.csv",
    "3. Random Split (Easier Data)": "models/finetune_v6_rdkit_random/replicate_*/model_0/test_predictions.csv",
    "4. Single Model (No Ensemble)": "models/finetune_v6_rdkit_single/model_0/test_predictions.csv",
    "5. Final Winning Model (Pretrain + RDKit + Ensemble)": "models/finetune_v6_rdkit_scaffold/replicate_*/model_0/test_predictions.csv"
}

results = []

for name, path_pattern in experiments.items():
    files = glob.glob(path_pattern)
    if not files:
        print(f"Could not find files for {name}")
        continue
        
    roc_aucs = []
    prc_aucs = []
    
    for f in files:
        # 2. Load predictions and rename the column
        df_pred = pd.read_csv(f)
        df_pred = df_pred[['smiles', 'activity']].rename(columns={'activity': 'pred_prob'})
        
        # 3. Safely merge based on the exact SMILES strings
        df_merged = pd.merge(df_pred, df_truth, on='smiles', how='inner')
        
        if df_merged.empty:
            continue
            
        y_true = df_merged['true_activity'].values
        y_prob = df_merged['pred_prob'].values
        
        # Calculate the metrics!
        roc_aucs.append(roc_auc_score(y_true, y_prob))
        prc_aucs.append(average_precision_score(y_true, y_prob))
        
    if not roc_aucs:
        continue
        
    # Average across the folds
    mean_roc = np.mean(roc_aucs)
    std_roc = np.std(roc_aucs)
    mean_prc = np.mean(prc_aucs)
    std_prc = np.std(prc_aucs)
    
    results.append({
        "Model Architecture": name,
        "Folds": len(roc_aucs),
        "ROC-AUC": f"{mean_roc:.4f} ± {std_roc:.4f}" if len(roc_aucs) > 1 else f"{mean_roc:.4f}",
        "PRC-AUC": f"{mean_prc:.4f} ± {std_prc:.4f}" if len(roc_aucs) > 1 else f"{mean_prc:.4f}"
    })

# Create and print the Markdown Table
df_results = pd.DataFrame(results)
print("\n### Table 1: Model Validation and Ablation Study")
print(df_results.to_markdown(index=False))

# Save to CSV for your records
df_results.to_csv("results/v6_ablation_metrics.csv", index=False)
print("\n Saved to results/v6_ablation_metrics.csv")
