import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="data/chroma_db")
collection = client.get_collection("mscac_projects")
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def match_student(student_input, n_results=3):
    query = f"{student_input['headline']}. {student_input['request']}"
    q_emb = embed_model.encode([query])
    res = collection.query(
        query_embeddings=q_emb,
        n_results=n_results,
        include=["metadatas", "documents", "distances"]
    )

    matches = []
    for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
        matches.append({
            "title": doc,
            "meta": meta,
            "distance": dist
        })

    top_meta = res["metadatas"][0][0]
    top_title = res["documents"][0][0]
    alumnus_name = top_meta.get("student", "the alumnus")

    email = f"""
Hi {alumnus_name},

{student_input['student_type']} {student_input['student_name']} just requested for advice on: {student_input['headline']}

A bit about them:
{student_input['background']}

They are seeking guidance on:
{student_input['request']}

Would you be open to connecting and sharing your experience on "{top_title}"?

{student_input['closing']}

Thanks,
MScAC Alumni Relations
"""

    return matches, email
