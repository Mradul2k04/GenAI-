import wikipedia
from langchain_community.retrievers import WikipediaRetriever


retrivers=WikipediaRetriever(top_k_results=2, lang='en')

query='The geopolitical history of India and pakistan from the perspective of a chinese'


docs=retrivers.invoke(query)

for i , docs in enumerate(docs):
    print(f"\n-----Result {i+1}-----")
    print(f"Content : \n {docs.page_content}..")