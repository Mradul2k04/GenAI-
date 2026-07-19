from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool=TavilySearchResults(
    max_result=5
)

models=ChatGroq(model="llama-3.1-8b-instant")

prompt=ChatPromptTemplate.from_template(
    """
    You are the helpful assistant
    
    summarize the following news into clear bullet points
    
    {news}
    
    """
)

parser=StrOutputParser()

chain=prompt |models | parser

news_result=search_tool.run("Latest AI news of 2026")

result=chain.invoke({"news":news_result})

print(result)




print(search_tool.description)
print(search_tool.name)
print(search_tool.args)