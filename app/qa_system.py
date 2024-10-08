from langchain import hub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.llms import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.config import OPEN_AI_API_KEY

def answer_question(question, retriever):
    llm = OpenAI(openai_api_key=OPEN_AI_API_KEY, temperature=0)

    system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)   

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(llm,prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    result = rag_chain.invoke({"input" : question})
    return result["answer"]