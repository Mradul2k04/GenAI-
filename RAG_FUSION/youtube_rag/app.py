from utils.logger import get_logger

from ingestion.transcript_loader import load_transcript
from ingestion.text_splitter import split_documents
from ingestion.vector_store import create_vector_store
from retrieval.retriever import get_retriever
from chains.rag_chain import build_rag_chain

logger = get_logger(__name__)


def main():

    logger.info("=" * 60)
    logger.info("Starting YouTube RAG Application")
    logger.info("=" * 60)

    video_id = input("Enter YouTube Video ID: ").strip()

    try:

        # Step 1: Load Transcript
        logger.info("Loading transcript...")
        transcript = load_transcript(video_id)

        # Step 2: Split Transcript
        logger.info("Splitting transcript...")
        chunks = split_documents(transcript)

        # Step 3: Create Vector Store
        logger.info("Creating FAISS vector database...")
        create_vector_store(chunks)

        # Step 4: Create Retriever
        logger.info("Creating retriever...")
        retriever = get_retriever()

        # Step 5: Build RAG Chain
        logger.info("Building RAG chain...")
        rag_chain = build_rag_chain(retriever)

        print("\n" + "=" * 70)
        print("YouTube RAG is Ready!")
        print("Type 'exit' to quit.")
        print("=" * 70)

        while True:

            question = input("\nAsk Your Question: ").strip()

            if question.lower() in ["exit", "quit"]:
                logger.info("Application closed by user.")
                print("Goodbye!")
                break

            logger.info(f"User Question: {question}")

            response = rag_chain.invoke(question)

            print("\nAnswer:\n")
            print(response)

    except Exception as e:
        logger.exception(f"Application Error: {e}")
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()