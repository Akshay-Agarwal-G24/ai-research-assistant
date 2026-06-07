import chromadb

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_collection(
    name="research_docs"
)

def retrieve_chunks(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results