from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="text-embedding-004",dimensions=32)

result=embedding.embed_query("Delhi is the Capital of India")

print(str(result))