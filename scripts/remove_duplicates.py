import pandas as pd

# 1. Load the library
df = pd.read_csv("screening_library.csv")
initial_count = len(df)

# 2. Strip CXSMILES tags (keeping only the standard SMILES part)
df['smiles'] = df['smiles'].astype(str).str.split().str[0]

# 3. Remove duplicates based on the SMILES column
# keep='first' ensures we keep the first occurrence of each molecule
df_unique = df.drop_duplicates(subset=['smiles'], keep='first')
final_count = len(df_unique)

# 4. Save to the final screening file
output_path = "screening_library_final.csv"
df_unique.to_csv(output_path, index=False)

print(f"Initial compounds: {initial_count}")
print(f"Duplicates removed: {initial_count - final_count}")
print(f"Final unique compounds: {final_count}")
print(f"File saved as: {output_path}")