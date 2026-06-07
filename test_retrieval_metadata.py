from utils.embeddings import create_embeddings
from utils.retrieve import retrieve_chunks

query = "What is MCP?"

query_embedding = create_embeddings([query])[0]

results = retrieve_chunks(query_embedding)

for i in range(len(results["chunks"])):

    print("\n" + "=" * 60)

    print("Distance:")
    print(results["distances"][i])

    print("\nMetadata:")
    print(results["metadata"][i])

    print("\nChunk Preview:")
    print(results["chunks"][i][:300])