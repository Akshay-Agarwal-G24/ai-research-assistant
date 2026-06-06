# test_pdf.py

from utils.ingest import extract_text_from_pdf

text = extract_text_from_pdf("data/sample.pdf")

print(text[:2000])