from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = CohereEmbeddings(model='embed-english-v3.0')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))