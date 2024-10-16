import os
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY = os.environ['OPEN_AI_API_KEY']

LANGCHAIN_TRACING_V2 = os.environ["LANGCHAIN_TRACING_V2"]
LANGCHAIN_API_KEY = os.environ["LANGCHAIN_API_KEY"]
LANGCHAIN_PROJECT = os.environ["LANGCHAIN_PROJECT"]