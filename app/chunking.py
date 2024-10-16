from langchain.text_splitter import CharacterTextSplitter


def chunk_text(text):
    text_splitter = CharacterTextSplitter(
        separator=".",
        chunk_size=1000,
        length_function=len,
        chunk_overlap=100,
    )
    return text_splitter.create_documents([text])


