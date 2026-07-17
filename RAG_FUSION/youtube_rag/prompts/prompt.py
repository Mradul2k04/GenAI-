from langchain_core.prompts import PromptTemplate

from utils.logger import get_logger

logger = get_logger(__name__)


def get_rag_prompt() -> PromptTemplate:
    """
    Returns the prompt template used by the RAG chain.
    """

    logger.info("Loading RAG prompt...")

    template = """
You are a helpful AI assistant.

Use ONLY the provided context to answer the user's question.

Instructions:
- Answer only from the context.
- Do not make up facts.
- If the answer is not available in the context, reply:
  "I don't know based on the provided transcript."
- Keep the answer concise and accurate.
- If appropriate, summarize information in bullet points.

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )

    logger.info("Prompt loaded successfully.")

    return prompt


if __name__ == "__main__":

    prompt = get_rag_prompt()

    print(prompt.format(
        context="LangChain is a framework for building LLM applications.",
        question="What is LangChain?"
    ))