def create_chunks(text, chunk_size=1000, overlap=100):
    paragraphs = text.split("\n\n")

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if len(current_chunk) + len(paragraph) <= chunk_size:
            current_chunk += paragraph + "\n\n"

        else:
            chunks.append(current_chunk.strip())

            overlap_text = current_chunk[-overlap:]

            current_chunk = overlap_text + "\n\n" + paragraph

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks