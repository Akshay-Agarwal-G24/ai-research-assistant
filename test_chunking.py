# test_chunking.py

from utils.ingest import (
    extract_text_from_pdf,
    chunk_text
)

text = extract_text_from_pdf(
    "data/sample.pdf"
)

chunks = chunk_text(text)

print(f"Number of chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])