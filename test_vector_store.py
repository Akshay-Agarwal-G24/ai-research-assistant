from utils.ingest import extract_text_from_pdf
from utils.chunker import create_chunks
from utils.embeddings import create_embeddings
from utils.vector_store import store_embeddings

pdf_path = "data/THE AGENTIC AI HANDBOOK.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = create_chunks(text)

embeddings = create_embeddings(chunks)

store_embeddings(chunks, embeddings)

print("Stored successfully!")