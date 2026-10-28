import fitz
from sentence_transformers import SentenceTransformer
from chunker import create_chunks
import re


def clean_text(text):
    # Join words broken across lines
    text = re.sub(r"-\n", "", text)

    # Replace newlines with spaces
    text = re.sub(r"\n", " ", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Open PDF
pdf_path = "data/papers/diabetes_ml.pdf"
document = fitz.open(pdf_path)


all_chunks = []


# Extract and chunk the paper
for page_number, page in enumerate(document):

    text = page.get_text()

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


# Get the text from every chunk
texts = [chunk["text"] for chunk in all_chunks]


# Generate embeddings
embeddings = model.encode(texts)


print("Embedding shape:", embeddings.shape)

print("First chunk:")
print(all_chunks[0]["text"])

print("\nFirst chunk embedding:")
print(embeddings[0][:10])