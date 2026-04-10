import pandas as pd
from pathlib import Path

print("Loading the Drug Repurposing Hub dataset...")

# Load the file. 
# sep='\t' handles the tab spacing.
# comment='!' automatically skips the metadata at the top of the file.
df = pd.read_csv("repo-sample-annotation-20240610.txt", sep='\t', comment='!', low_memory=False)

# Select only the columns we need: SMILES (for the model) and the Drug Name/ID (for you)
df_clean = df[['smiles', 'pert_iname', 'broad_id']].copy()

# Drop any rows that are missing a SMILES string (Chemprop will crash without them)
df_clean = df_clean.dropna(subset=['smiles'])

# Save to a clean CSV file
output_file = "screening_library.csv"
df_clean.to_csv(output_file, index=False)

print(f"Successfully prepared {len(df_clean)} compounds!")
print(f"File saved as: {output_file}")