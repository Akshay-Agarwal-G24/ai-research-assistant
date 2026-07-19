from utils.embeddings import create_query_embedding
from utils.retrieve import retrieve_chunks
from utils.llm import ask_llm
from utils.memory import (
    get_history,
    add_message
)
from utils.query_rewriter import rewrite_question


def ask_question(question):

    history = get_history()

    if history:
        rewrite_result = rewrite_question(
        history[-4:],
        question
    )
        if rewrite_result["success"]:
            standalone_question = rewrite_result["question"]
        else:
            standalone_question = question
    else:
        standalone_question = question

    """ print(
    f"\nStandalone Question: {standalone_question}\n"
    ) """

    query_embedding = create_query_embedding(standalone_question)

    results = retrieve_chunks(query_embedding)

    #chunks = results["documents"][0]
    chunks = results["chunks"]

    best_distance = results["distances"][0]

    if best_distance > 1.3:

        answer = (
        "I could not find the answer "
        "in the provided documents."
        )

        add_message("user", question)
        add_message("assistant", answer)

        return {
            "answer": answer,
            "sources": [],
            "debug": {
                "retrieved_chunks": [],
                "retrieval_distances": results["distances"]
            }
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
{standalone_question}
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

    add_message("user", question)
    add_message("assistant", answer)        

    return {
        "answer": answer,
        "sources": sources,
        "debug": {
            "retrieved_chunks": chunks,
            "retrieval_distances": results["distances"]
            }
    }