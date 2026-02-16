import config
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from os import getenv
from pinecone import Pinecone

try:
    pc = Pinecone()
except Exception as e:
    raise e
try:
    #     model = ChatOpenAI(
    #         api_key=getenv("OPENROUTER_API_KEY"),
    #         base_url="https://openrouter.ai/api/v1",
    #         model="tngtech/deepseek-r1t2-chimera:free",
    #     )
    #     print("Successfully initialized model with OpenRouter")
    # except Exception as e:
    # print("Failed to initialize model with OpenRouter: ", e)
    model = ChatOpenAI(model="gpt-4o", temperature=1, max_retries=3)
except Exception as e:
    raise e
