from utils.ingest import extract_pages_from_pdf

pages = extract_pages_from_pdf(
    "data/THE AGENTIC AI HANDBOOK.pdf"
)

print(f"Total Pages: {len(pages)}")

print("\nFirst Page Metadata:")
print(pages[0]["page"])

print("\nFirst 500 Characters:")
print(pages[0]["text"][:500])