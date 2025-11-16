import pandas as pd
import os
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

# Paths
clean_csv = os.path.join("data", "projects_clean.csv")
embeddings_file = os.path.join("data", "projects_embeddings.pkl")
metadata_file = os.path.join("data", "projects_metadata.pkl")

# Load cleaned CSV
df = pd.read_csv(clean_csv)

# Initialize sentence-transformers model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
texts = df["combined_text"].tolist()
embeddings = model.encode(texts, show_progress_bar=True)

# Convert to numpy array
embeddings = np.array(embeddings)

# Save embeddings
with open(embeddings_file, "wb") as f:
    pickle.dump(embeddings, f)

# Save metadata (dict per record for Chroma)
metadata = df[[
    "project_id",
    "student",
    "partner",
    "cohort",
    "concentration",
    "internship_title_(aria)",
    "partner_supervisor",
    "academic_supervisor"
]].to_dict(orient="records")

with open(metadata_file, "wb") as f:
    pickle.dump(metadata, f)

print("Embeddings saved to:", embeddings_file)
print("Metadata saved to:", metadata_file)