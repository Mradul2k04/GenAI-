from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

from dotenv import load_dotenv

load_dotenv()


import os

os.environ['HF_HOME']='D:/hugging_face_cache'

llm=HuggingFacePipeline.from_model_id(
    model_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=500
    )
)
model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the Capital of India")

print(result.content)