from utils.ingest import extract_pages_from_pdf
from utils.chunker import chunk_pages

pages = extract_pages_from_pdf(
    "data/THE AGENTIC AI HANDBOOK.pdf"
)

chunked_pages = chunk_pages(pages)

print(f"Total Chunk Objects: {len(chunked_pages)}")

print("\nFirst Chunk:")

print("Page:", chunked_pages[0]["page"])

print(chunked_pages[0]["chunk"][:500])