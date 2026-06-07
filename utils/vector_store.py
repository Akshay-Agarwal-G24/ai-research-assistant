import chromadb

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="research_docs"
)

""" def store_embeddings(chunks, embeddings):

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    ) """

def store_embeddings(chunked_pages, embeddings, source_file):

    ids = []
    documents = []
    metadatas = []

    for i, chunk_obj in enumerate(chunked_pages):

        ids.append(f"chunk_{i}")

        documents.append(
            chunk_obj["chunk"]
        )

        metadatas.append(
            {
                "source": source_file,
                "page": chunk_obj["page"]
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )