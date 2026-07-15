from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(r'C:\Users\Acer\OneDrive\Desktop\GenAI\Document_Loaders\GenAI_LangChain_DeepDive_Notes.pdf', )

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_documents(docs)

print(result[0])