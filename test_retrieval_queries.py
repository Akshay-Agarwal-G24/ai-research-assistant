from utils.embeddings import create_query_embedding
from utils.retrieve import retrieve_chunks

queries = [
    "What is MCP?",
    "What is Model Context Protocol?",
    "What is reinforcement learning?",
    "What are goals in agentic AI?",
    "What is planning in agentic AI?"
]

for query in queries:

    query_embedding = create_query_embedding(query)

    results = retrieve_chunks(query_embedding)

    best_distance = results["distances"][0][0]

    print("=" * 80)
    print(f"Query: {query}")
    print(f"Best Distance: {best_distance}")

    # Optional: print the top retrieved chunk preview
    top_chunk = results["documents"][0][0]

    print("\nTop Retrieved Chunk Preview:")
    print(top_chunk[:300].replace("\n", " "))

    print("\n")