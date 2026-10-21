import fitz

pdf_path = "data/papers/diabetes_ml.pdf"

document = fitz.open(pdf_path)

print("Number of pages:", len(document))

for page_number, page in enumerate(document):
    text = page.get_text()

    print(f"\n--- PAGE {page_number + 1} ---")
    print(text[:1000])