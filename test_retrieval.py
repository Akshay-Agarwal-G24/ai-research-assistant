from utils.embeddings import create_query_embedding
from utils.retrieve import retrieve_chunks

query = "What is Agentic AI?"

query_embedding = create_query_embedding(query)

results = retrieve_chunks(query_embedding)

#print(results)

for i, doc in enumerate(results["documents"][0]):

    print(f"\nResult {i+1}")
    print("-" * 50)

    print(doc[:500])

    print(
        f"Score: {results['distances'][0][i]}"
    )