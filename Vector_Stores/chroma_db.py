from langchain_cohere import CohereEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = CohereEmbeddings(model='embed-english-v3.0')

documents = [
    "Virat Kohli is a batsman",
    "MS Dhoni is a wicketkeeper",
    "Jasprit Bumrah is a bowler"
]

vectorstore=Chroma.from_texts(
    documents,
    embeddings,
    persist_directory='.\chroma_db'
)

result=vectorstore.similarity_search(
    'who is Bumrah',
    k=1
)

#print(result[0].page_content)
#print(vectorstore.get(include=['embeddings','documents']))
print(vectorstore.asimilarity_search_with_score(
    'Who among these are a bowler',
    k=2
))
