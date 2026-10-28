import fitz
import re
from chunker import create_chunks


def clean_text(text):
    # Join words broken across lines
    text = re.sub(r"-\n", "", text)

    # Replace single newlines with spaces
    text = re.sub(r"\n", " ", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


pdf_path = "data/papers/diabetes_ml.pdf"

document = fitz.open(pdf_path)

all_chunks = []

for page_number, page in enumerate(document):

    text = page.get_text()

    # Clean PDF text
    text = clean_text(text)

    chunks = create_chunks(text)

    for chunk_number, chunk in enumerate(chunks):

        chunk_data = {
            "document_id": "diabetes_ml",
            "page": page_number + 1,
            "chunk_id": f"diabetes_ml_p{page_number + 1}_c{chunk_number + 1}",
            "text": chunk
        }

        all_chunks.append(chunk_data)


print("Total chunks:", len(all_chunks))

for chunk in all_chunks[:5]:

    print("\n==============================")
    print("Document:", chunk["document_id"])
    print("Page:", chunk["page"])
    print("Chunk ID:", chunk["chunk_id"])
    print("Text:")
    print(chunk["text"])