""" from utils.ingest import extract_text_from_pdf
from utils.chunker import create_chunks """
from utils.ingest import extract_pages_from_pdf
from utils.chunker import chunk_pages
from utils.embeddings import create_embeddings
from utils.vector_store import store_embeddings

pdf_path = "data/THE AGENTIC AI HANDBOOK.pdf"

""" text = extract_text_from_pdf(pdf_path)

chunks = create_chunks(text)
 """
pages = extract_pages_from_pdf(pdf_path)

chunked_pages = chunk_pages(pages)

""" print(type(chunked_pages))
print(type(chunked_pages[0]))
print(chunked_pages[0])
 """
chunks = [
    chunk_obj["chunk"]
    for chunk_obj in chunked_pages
]

#chunked_pages = chunk_pages(pages)

embeddings = create_embeddings(chunks)

store_embeddings(chunked_pages, embeddings, "THE AGENTIC AI HANDBOOK.pdf")

print("Stored successfully!")