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

            response = ask_question(benchmark["question"])

            self.results.append({
                "benchmark": benchmark,
                "response": response
            })

        return self.results    