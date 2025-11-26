import os, json, pickle, chromadb
from sentence_transformers import SentenceTransformer

def rebuild():
    os.makedirs("data/chroma_db", exist_ok=True)

    client = chromadb.PersistentClient(path="data/chroma_db")
    collection = client.get_or_create_collection(
        "mscac_projects",
        metadata={"description": "MScAC alumni internship projects"}
    )

    # Load metadata (must be committed to repo)
    with open("data/others/projects_metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    docs = [m.get("internship_title_(aria)", "") for m in metadata]

    # Recompute embeddings fresh for safety
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(docs).tolist()

    # Ensure metadata is JSON-serializable
    for m in metadata:
        json.dumps(m)

    ids = [str(i) for i in range(len(metadata))]

    collection.add(
        documents=docs,
        metadatas=metadata,
        embeddings=embeddings,
        ids=ids
    )

    print("Rebuilt ChromaDB successfully.")