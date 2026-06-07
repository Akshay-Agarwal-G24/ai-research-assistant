import chromadb

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="research_docs"
)

def store_embeddings(chunks, embeddings):

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )