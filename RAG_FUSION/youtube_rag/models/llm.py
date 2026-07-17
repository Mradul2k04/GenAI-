from langchain_groq import ChatGroq
from langchain_cohere import CohereEmbeddings
from utils.logger import get_logger
from config.settings import MODEL_NAME

logger = get_logger(__name__)

def load_llm():
    logger.info(f"Loading Groq Model: {MODEL_NAME}")
    try:
        llm = ChatGroq(
            model=MODEL_NAME,
            temperature=0,
            max_tokens=1024
        )

        logger.info("Groq model loaded successfully.")
        return llm
    except Exception as e:
        logger.exception(f"Failed to initialize Groq LLM: {e}")
        raise
    
if __name__ == "__main__":

    logger.info("Testing Groq LLM...")

    llm = load_llm()

    response = llm.invoke("Who is the Prime Minister of India?")

    print(response.content)