import time

from evaluation.benchmark import BENCHMARK_DATASET
from utils.rag import ask_question
from evaluation.metrics import calculate_metrics

class RAGEvaluator:
    def __init__(self):
        self.results = []
        self.config = {
            "similarity_threshold": 0.85
        }

    def run(self):
        self.results.clear()

        for benchmark in BENCHMARK_DATASET:

            status = "Success"
            error = None

            try:
                response = ask_question(benchmark["question"])

                metrics = calculate_metrics(benchmark, response, self.config)

            except Exception as e:
                print(f"\nBenchmark failed!")
                print(f"Question: {benchmark['question']}")
                print(f"Exception Type: {type(e).__name__}")
                print(f"Exception: {e}")

                status = "Failed"
                error = str(e)
                response = None
                metrics = None

            self.results.append({
                "benchmark": benchmark,
                "response": response,
                "metrics": metrics,
                "status": status,
                "error": error
            })

            time.sleep(20)  # Optional: Add a small delay between evaluations

        summary = self.generate_summary()

        return {
            "results": self.results,
            "summary": summary
        }

    def generate_summary(self):
        # TODO:
        # Separate runtime failures from evaluation failures.
        # summary = {
        #     "total_benchmarks": 5,
        #     "evaluated": 4,
        #     "runtime_failures": 1,
        #     "passed": 3,
        #     "failed": 1,
        #     "pass_rate": 75.0
        # }

        total = len(self.results)
        valid_results = [result for result in self.results if result["metrics"] is not None]
        passed = sum(1 for result in valid_results if result["metrics"]["semantic_similarity"]["passed"])
        failed = total - passed

        pass_rate = (passed / total) * 100 if total > 0 else 0
        
        scores = [
            result["metrics"]["semantic_similarity"]["score"]
            for result in valid_results
            if result["metrics"]["semantic_similarity"]["score"] is not None
        ]

        average_similarity = (
            sum(scores) / len(scores)
            if scores else 0
        )

        summary = {
            "total_benchmarks": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": pass_rate,
            "average_semantic_similarity": round(average_similarity, 2)
        }

        return summary    