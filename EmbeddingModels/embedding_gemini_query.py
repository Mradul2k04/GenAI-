from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = CohereEmbeddings(
    model="embed-english-v3.0"
)
# vector = embeddings.embed_query("What is the capital of India?")
# print(len(vector))

docs = [
    "Delhi is the capital of India.",
    "Paris is the capital of France."
]

vectors = embeddings.embed_documents(docs)
print(len(vectors))
print(len(vectors[0]))