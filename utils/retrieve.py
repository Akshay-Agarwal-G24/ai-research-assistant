import chromadb

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_collection(
    name="research_docs"
)

def retrieve_chunks(query_embedding, top_k=10):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,
        include=[
            "documents",
            "distances",
            "metadatas"
        ]
    )

    #return results
    return {
        "chunks": results["documents"][0],
        "distances": results["distances"][0],
        "ids": results["ids"][0],
        "metadata": results["metadatas"][0]
    }