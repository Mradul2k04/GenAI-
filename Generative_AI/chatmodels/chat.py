from dotenv import load_dotenv


load_dotenv()

## from langchain.chat_models import init_chat_model ##init_model

from langchain_google_genai import ChatGoogleGenerativeAI

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite") ## Model Class

#print(model)

response=model.invoke("Tell me about GLA UNIVERSITY")

print(response.content)