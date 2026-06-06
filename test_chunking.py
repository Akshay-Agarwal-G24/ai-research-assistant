# test_chunking.py

from utils.ingest import (
    extract_text_from_pdf,
    chunk_text
)

text = extract_text_from_pdf(
    "data/THE AGENTIC AI HANDBOOK.pdf"
)

chunks = chunk_text(text)

print(f"Number of chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

for i, chunk in enumerate(chunks[:3]):
    print(f"\nChunk {i+1}")
    print("=" * 50)
    print(chunk[:300])