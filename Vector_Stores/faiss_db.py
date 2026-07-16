from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "Virat Kohli is a batsman",
    "MS Dhoni is a wicketkeeper",
    "Jasprit Bumrah is a bowler"
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = FAISS.from_texts(
    documents,
    embeddings
)

results = vectorstore.similarity_search(
    'Tell me about Dhoni',
    k=1
)

print(results[0].page_content)

vectorstore.save_local("faiss_index")