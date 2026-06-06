from utils.ingest import extract_text_from_pdf
from utils.chunker import create_chunks
from utils.embeddings import create_embeddings

pdf_path = "data/THE AGENTIC AI HANDBOOK.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = create_chunks(text)

embeddings = create_embeddings(chunks)

print(f"Number of chunks: {len(chunks)}")
print(f"Number of embeddings: {len(embeddings)}")
print(f"Embedding dimensions: {len(embeddings[0])}")

print(type(embeddings))
print(type(embeddings[0]))
print(embeddings[0][:5])