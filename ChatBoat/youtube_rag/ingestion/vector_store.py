from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document

from config.settings import EMBED_MODEL, VECTOR_DB_PATH
from utils.logger import get_logger

logger = get_logger(__name__)

# Initialize embedding model
embeddings = CohereEmbeddings(
    model=EMBED_MODEL
)


def create_vector_store(documents: list[Document]) -> FAISS:
    """
    Create a FAISS vector store from documents and save it locally.

    Args:
        documents (list[Document]): List of LangChain documents.

    Returns:
        FAISS: Created vector store.
    """

    logger.info("Creating FAISS vector store...")

    try:
        db = FAISS.from_documents(
            documents,
            embeddings
        )

        logger.info("FAISS vector store created successfully.")

        db.save_local(VECTOR_DB_PATH)

        logger.info(f"Vector store saved at: {VECTOR_DB_PATH}")

        return db

    except Exception as e:
        logger.exception(f"Failed to create vector store: {e}")
        raise


def load_vector_store() -> FAISS:
    """
    Load an existing FAISS vector store.

    Returns:
        FAISS: Loaded vector store.
    """

    logger.info("Loading FAISS vector store...")

    try:
        db = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        logger.info("Vector store loaded successfully.")

        return db

    except FileNotFoundError:
        logger.error(
            "Vector store not found. Please create it first."
        )
        raise

    except Exception as e:
        logger.exception(f"Failed to load vector store: {e}")
        raise


if __name__ == "__main__":

    logger.info("Testing Vector Store...")

    docs = [
        Document(page_content="LangChain is a framework for LLM applications."),
        Document(page_content="FAISS is a vector database."),
        Document(page_content="Groq provides ultra-fast LLM inference.")
    ]

    db = create_vector_store(docs)

    logger.info(f"Number of vectors stored: {db.index.ntotal}")

    loaded_db = load_vector_store()

    logger.info(f"Loaded vectors: {loaded_db.index.ntotal}")

    print("Vector Store Test Successful ✅")
    