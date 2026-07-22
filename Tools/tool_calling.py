from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from rich import print
 
#Creating Tools
@tool
def get_text_length(text : str)->int:
    """Return the number of Character in a given text"""
    return len(text)
tools={
    "get_text_length":get_text_length
}

model=ChatGroq(model="llama-3.1-8b-instant")

#tool binding
model_with_tool=model.bind_tools([get_text_length])

message=[]
prompt=input("You: ")
query=HumanMessage(prompt)
message.append(query)


result=model_with_tool.invoke(message)
message.append(result)

if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_message)

result = model_with_tool.invoke(message)
print(result.content)