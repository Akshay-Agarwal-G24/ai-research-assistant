# test_recursive_chunking.py

from utils.ingest import extract_text_from_pdf
from utils.chunker import create_chunks

text = extract_text_from_pdf(
    "data/THE AGENTIC AI HANDBOOK.pdf"
)

chunks = create_chunks(text)

print("Number of chunks:", len(chunks))

for i in range(3):
    print(f"\nChunk {i+1}")
    print("=" * 50)
    print(chunks[i][:300])