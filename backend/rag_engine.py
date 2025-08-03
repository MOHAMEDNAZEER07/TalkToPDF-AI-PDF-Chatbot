from model_config import embedder, get_gemini_response
from utils import extract_text_from_pdf, chunk_text

import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="./chroma_db")

collection_name = "pdf_chunks"
if collection_name in [col.name for col in client.list_collections()]:
    collection = client.get_collection(name=collection_name)
else:
    collection = client.create_collection(name=collection_name)

def ingest_pdf(path):
    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)
    embeddings = embedder.encode(chunks).tolist()

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[str(i)]
        )

def query_rag(user_query):
    query_embedding = embedder.encode([user_query])[0].tolist()

    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    documents = results.get("documents", [[]])[0]

    if not documents:
        return "⚠️ No relevant context found in the database."

    context = "\n".join(documents)

    prompt = f"""Answer the question based only on the context below:

Context: {context}

Question: {user_query}
Answer:"""

    return get_gemini_response(prompt)
