import pandas as pd

# Load the library you just created
df = pd.read_csv("screening_library.csv")

# Strip out the CXSMILES tags (everything after the first space)
# Example: "CCO |abc|" becomes "CCO"
df['smiles'] = df['smiles'].astype(str).str.split().str[0]

# Save as a new 'clean' file
df.to_csv("screening_library_clean.csv", index=False)

print(f"Cleaned {len(df)} SMILES strings.")
print("Saved to: screening_library_clean.csv")