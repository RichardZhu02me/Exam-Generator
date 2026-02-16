import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# You can add validaton here if needed
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables")
if not os.getenv("PINECONE_API_KEY"):
    raise ValueError("PINECONE_API_KEY not found in environment variables")
if not os.getenv("OPENROUTER_API_KEY"):
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")
