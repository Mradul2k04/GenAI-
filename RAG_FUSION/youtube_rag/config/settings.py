import os 
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.3-70b-versatile"
)

EMBED_MODEL = os.getenv(
    "EMBED_MODEL",
    "embed-english-v3.0"
)

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "data/faiss_index"
)