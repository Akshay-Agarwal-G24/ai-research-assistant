# test_pdf.py

from utils.ingest import extract_text_from_pdf

text = extract_text_from_pdf("data/THE AGENTIC AI HANDBOOK.pdf")

print(text[:2000])