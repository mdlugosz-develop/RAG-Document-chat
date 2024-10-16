from langchain_community.llms import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
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
            ("human", "{question}"),
        ]
    )

    chain = {"context" : retriever, "question" : RunnablePassthrough() } | prompt | llm | StrOutputParser()

    return chain.invoke(question)
    