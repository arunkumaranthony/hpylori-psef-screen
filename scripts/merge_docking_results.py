import pandas as pd
import sys
from pathlib import Path

# Dynamically set paths to the 'results' folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DL_RESULTS_FILE = PROJECT_ROOT / "results" / "screening_results.csv"
DOCKING_RESULTS_FILE = PROJECT_ROOT / "results" / "model_01_psef_protein_binding_energy.csv"
OUTPUT_FILE = PROJECT_ROOT / "results" / "final_hit_list.csv"

def merge_consensus(dl_file, docking_file, output_path):
    print("Merging Deep Learning predictions with Docking energies...")

    if not dl_file.exists() or not docking_file.exists():
        print("Error: Missing input files in the 'results' folder.")
        sys.exit(1)

    try:
        df_dl = pd.read_csv(dl_file)
        df_docking = pd.read_csv(docking_file)

        # Perform the merge
        df_consensus = pd.merge(
            df_dl,
            df_docking[['Ligand', 'Binding Energy (kcal/mol)']],
            left_on='pert_iname',
            right_on='Ligand',
            how='inner'
        )

        # Clean up redundant column
        if 'Ligand' in df_consensus.columns:
            df_consensus = df_consensus.drop(columns=['Ligand'])

        # Sort the results
        target_col = 'activity' if 'activity' in df_consensus.columns else df_consensus.columns[1]
        df_consensus = df_consensus.sort_values(
            by=[target_col, 'Binding Energy (kcal/mol)'], 
            ascending=[False, True]
        )

        df_consensus.to_csv(output_path, index=False)
        print(f"Successfully merged {len(df_consensus)} compounds!")
        print(f"Consensus hit list saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred during the merge: {e}")

if __name__ == "__main__":
    merge_consensus(DL_RESULTS_FILE, DOCKING_RESULTS_FILE, OUTPUT_FILE)