from evaluation.evaluator import RAGEvaluator

result = RAGEvaluator().run()

print("Evaluation Results:")
for idx, res in enumerate(result["results"]):
    print(f"\nBenchmark {idx + 1}:")
    print("Question:", res["benchmark"]["question"])
    print("Answer:", res["response"]["answer"])
    print("Sources:", res["response"]["sources"])
    print("Metrics:", res["metrics"])
    print("Status:", res["status"])
    if res["error"]:
        print("Error:", res["error"])

print("\nSummary:")
summary = result["summary"]
for metric, value in summary.items():
    print(f"{metric.capitalize()}: {value}")