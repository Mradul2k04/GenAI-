from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils.logger import get_logger

logger = get_logger(__name__)


def split_documents(transcript: str):
    """
    Split transcript into chunks.

    Args:
        transcript (str): Transcript text.

    Returns:
        list[Document]
    """

    logger.info("Splitting transcript into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.create_documents([transcript])

    logger.info(f"Created {len(chunks)} chunks.")

    return chunks
if __name__ == "__main__":
    chunks = split_documents()

    print(f"Total Chunks: {len(chunks)}")

    if len(chunks) > 100:
        print(chunks[100])
    else:
        logger.warning("Less than 101 chunks created.")