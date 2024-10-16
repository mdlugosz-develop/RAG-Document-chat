from app.config import OPEN_AI_API_KEY
import chromadb
from langchain_community.embeddings import OpenAIEmbeddings
from app.interface import create_interface
from langchain_chroma import Chroma


file_path = "/Users/mati/Desktop/TakingItSerious/RAG-Document-chat/app/sample.txt"

embeddings = OpenAIEmbeddings(openai_api_key=OPEN_AI_API_KEY)


def main():

    client = chromadb.PersistentClient('/Users/mati/Desktop/TakingItSerious/RAG-Document-chat/app/db')

    vector_store_from_client = Chroma(
        client=client,
        collection_name='documents',
        embedding_function=embeddings
    )

    retriever = vector_store_from_client.as_retriever()
    demo = create_interface(vector_store_from_client,retriever)
    demo.launch()

if __name__ == "__main__":
    main()