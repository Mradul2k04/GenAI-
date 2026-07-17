from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda,
    RunnablePassthrough
)

from langchain_core.output_parsers import StrOutputParser

from prompts.prompt import get_rag_prompt
from models.llm import load_llm
from utils.helper import format_docs
from utils.logger import get_logger

logger = get_logger(__name__)


def build_rag_chain(retriever):

    logger.info("Building RAG Chain...")

    try:
        llm = load_llm()
        prompt = get_rag_prompt()

        chain = (
            RunnableParallel(
                {
                    "context": retriever | RunnableLambda(format_docs),
                    "question": RunnablePassthrough(),
                }
            )
            | prompt
            | llm
            | StrOutputParser()
        )

        logger.info("RAG Chain built successfully.")

        return chain

    except Exception as e:
        logger.exception(f"Failed to build RAG chain: {e}")
        raise


if __name__ == "__main__":

    from retrieval.retriever import get_retriever

    retriever = get_retriever()

    rag_chain = build_rag_chain(retriever)

    question = "Summarize the video."

    response = rag_chain.invoke(question)

    print("\nResponse:\n")
    print(response)