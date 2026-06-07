from utils.embeddings import create_query_embedding
from utils.retrieve import retrieve_chunks
from utils.llm import ask_llm


def ask_question(question):

    query_embedding = create_query_embedding(question)

    results = retrieve_chunks(query_embedding)

    #chunks = results["documents"][0]
    chunks = results["chunks"]

    best_distance = results["distances"][0]

    if best_distance > 1.3:
        #return "I could not find the answer in the provided documents."
        return {
            "answer": "I could not find the answer in the provided documents.",
            "sources": []
        }

    context = ""

    for i, chunk in enumerate(chunks):
        context += f"Chunk {i+1}:\n{chunk}\n\n"

    prompt = f"""
You are a helpful AI research assistant.

Use only the information provided in the context below to answer the question.

If the answer cannot be found in the context, say:
"I could not find the answer in the provided documents."

Context:
{context}

Question:
{question}
"""
    #print(f"Best Distance: {best_distance}")

    # return ask_llm(prompt)

    answer = ask_llm(prompt)

    sources = []

    for metadata in results["metadata"]:

        source_info = (
            f'{metadata["source"]} '
            f'(Page {metadata["page"]})'
        )

        if source_info not in sources:
            sources.append(source_info)

    return {
        "answer": answer,
        "sources": sources
    }