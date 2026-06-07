# utils/chunker.py

from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks

def chunk_pages(pages):

    chunked_pages = []

    for page in pages:

        chunks = create_chunks(page["text"])

        for chunk in chunks:

            chunked_pages.append(
                {
                    "chunk": chunk,
                    "page": page["page"]
                }
            )

    return chunked_pages