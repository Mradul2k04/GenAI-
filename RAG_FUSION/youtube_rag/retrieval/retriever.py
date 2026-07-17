from ingestion.vector_store import load_vector_store
from utils.logger import get_logger
from langchain_core.vectorstores import VectorStoreRetriever


logger = get_logger(__name__)

def get_retriever(
    search_type: str = "similarity",
    k: int = 4
):
    """
    Load the FAISS vector database and return a retriever.

    Args:
        search_type (str): Retrieval strategy.
                           Options:
                           - similarity
                           - mmr
                           - similarity_score_threshold

        k (int): Number of relevant documents to retrieve.

    Returns:
        BaseRetriever
    """
    logger.info("Loading vector store...")
    
    try:

        vector_store = load_vector_store()
        
        logger.info("Creating retriever...")

        retriever = vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={
                "k": k
            }
        )

        logger.info("Retriever created successfully.")

        return retriever
    except Exception as e:
        logger.exception(f"Failed to create retriever: {e}")
        raise
    
if __name__ == "__main__":

    logger.info("Testing Retriever...")

    retriever = get_retriever()

    query = "What is DeepMind?"

    docs = retriever.invoke(query)

    logger.info(f"Retrieved {len(docs)} documents.")

    print("\nRetrieved Documents:\n")

    for i, doc in enumerate(docs, start=1):
        print(f"Document {i}")
        print("-" * 60)
        print(doc.page_content[:500])
        print()