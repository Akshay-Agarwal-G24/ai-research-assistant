from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    trust_remote_code=False
)

print("Model loaded successfully!")