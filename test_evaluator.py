from evaluation.evaluator import RAGEvaluator

result = RAGEvaluator().run()

print("Evaluation Results:")
for idx, res in enumerate(result["results"]):
    
    print(f"\nBenchmark {idx + 1}:")
    print("Question:", res["benchmark"]["question"])
    print("Actual Answer:", res["response"]["answer"])
    print("Expected Answer:", res["benchmark"]["expected_answer"])
    print("Sources:", res["response"]["sources"])
    print("Metrics:", res["metrics"])
    print("Status:", res["status"])
    if res["error"]:
        print("Error:", res["error"])
    if(not res["metrics"]["semantic_similarity"]["passed"]):
        print("Retrieved Chunks:")
        for i, chunk in enumerate(res["response"]["debug"]["retrieved_chunks"]):
            print(f"Chunk {i + 1}:", chunk)
        print("Retrieval Distances:", res["response"]["debug"]["retrieval_distances"])

print("\nSummary:")
summary = result["summary"]
for metric, value in summary.items():
    print(f"{metric.capitalize()}: {value}")