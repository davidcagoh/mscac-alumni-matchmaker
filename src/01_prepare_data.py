import pandas as pd
import os

path = os.path.join("data", "projects.csv")
df = pd.read_csv(path)

# Normalize column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Columns to combine for embeddings
cols_to_combine = [
    "student",
    "partner",
    "internship_title_(aria)",
    "project_description",
    "public_abstract_(aria)",
    "concentration"
]

df["combined_text"] = df[cols_to_combine].astype(str).agg(" ".join, axis=1)

# Save cleaned CSV
out_path = os.path.join("data", "projects_clean.csv")
df.to_csv(out_path, index=False)

print("Saved cleaned CSV:", out_path)