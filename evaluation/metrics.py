from utils.embeddings import create_query_embedding
from scipy.spatial import distance

def semantic_similarity(
    expected_answer,
    actual_answer,
    threshold
):
    # TODO:
    # If the benchmark dataset grows significantly,
    # consider precomputing and caching expected-answer embeddings
    # to avoid recomputing them on every evaluation run.

    expected_embedding = create_query_embedding(expected_answer)

    actual_embedding = create_query_embedding(actual_answer)

    # scipy returns cosine distance. Convert it to cosine similarity.
    similarity = 1 - distance.cosine(expected_embedding, actual_embedding)

    return {"score": float(similarity), "threshold": threshold, "passed": similarity >= threshold}


def calculate_metrics(
    benchmark,
    response,
    config
):
    expected_answer = benchmark["expected_answer"]
    actual_answer = response["answer"]
    threshold = config["similarity_threshold"]

    try:
        semantic_similarity_result = semantic_similarity(expected_answer, actual_answer, threshold)
    except Exception as e:
        return {
        "semantic_similarity": {
            "score": None,
            "threshold": threshold,
            "passed": False,
            "error": str(e)
        }
    }

    return {"semantic_similarity": semantic_similarity_result}