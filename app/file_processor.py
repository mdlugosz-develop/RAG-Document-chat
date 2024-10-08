from uuid import uuid4
from app.chunking import chunk_text

def process_file(file, vector_store):
    content = open(file, 'r').read()
    documents = chunk_text(content)
    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=uuids)
    return documents