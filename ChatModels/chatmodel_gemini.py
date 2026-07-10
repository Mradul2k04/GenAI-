from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model =ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature=0,
    max_output_tokens=1000,
    model_kwargs={
        "tools": [{"googl e_search": {}}] 
    }
)

response=model.invoke("What is the Gold Rate Today")

print(response.content)