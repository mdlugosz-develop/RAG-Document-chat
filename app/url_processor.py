import requests
from app.chunking import chunk_text
from uuid import uuid4
from bs4 import BeautifulSoup
import re

def process_url(url, vector_store):
    response = requests.get(url)
    content = response.text
    documents = chunk_text(content)
    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=uuids)
    return documents

def process_wikipedia(url, vector_store):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    content_div = soup.find(id = 'mw-content-text')

    paragraphs = content_div.find_all('p')

    text = " ".join([para.get_text() for para in paragraphs])

    clean_text = re.sub(r'\[\d+\]', '', text)

    clean_text = " ".join(clean_text.split())

    documents = chunk_text(clean_text)

    uuids = [str(uuid4()) for _ in range(len(documents))]

    vector_store.add_documents(documents=documents, ids=uuids)

    return documents

