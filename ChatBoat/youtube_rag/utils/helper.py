"""
helper.py

Utility functions used throughout the YouTube RAG application.
"""

import os
import re
from typing import List

from langchain_core.documents import Document


def extract_video_id(url_or_id: str) -> str:
    """
    Extract YouTube Video ID from a URL or return the ID if already provided.

    Supported formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - VIDEO_ID

    Args:
        url_or_id (str): YouTube URL or Video ID.

    Returns:
        str: YouTube Video ID.

    Raises:
        ValueError: If the input is not a valid YouTube URL or ID.
    """

    patterns = [
        r"(?:v=)([A-Za-z0-9_-]{11})",
        r"(?:youtu\.be/)([A-Za-z0-9_-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)

    if len(url_or_id.strip()) == 11:
        return url_or_id.strip()

    raise ValueError("Invalid YouTube URL or Video ID.")


def format_docs(documents: List[Document]) -> str:
    """
    Convert retrieved LangChain Documents into a single context string.

    Args:
        documents (List[Document]): Retrieved documents.

    Returns:
        str: Formatted context.
    """

    return "\n\n".join(doc.page_content for doc in documents)


def clean_text(text: str) -> str:
    """
    Remove unnecessary whitespace.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text.
    """

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def ensure_directory(path: str) -> None:
    """
    Create directory if it doesn't exist.

    Args:
        path (str): Directory path.
    """

    os.makedirs(path, exist_ok=True)


def save_text(file_path: str, text: str) -> None:
    """
    Save text to a file.

    Args:
        file_path (str): Destination file.
        text (str): Text content.
    """

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)


def load_text(file_path: str) -> str:
    """
    Load text from a file.

    Args:
        file_path (str): Source file.

    Returns:
        str: File contents.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def print_separator(length: int = 70) -> None:
    """
    Print a separator line.

    Args:
        length (int): Length of separator.
    """

    print("=" * length)


def print_title(title: str) -> None:
    """
    Print a formatted title.

    Args:
        title (str): Title text.
    """

    print_separator()
    print(title)
    print_separator()


def validate_question(question: str) -> bool:
    """
    Validate user question.

    Args:
        question (str): User question.

    Returns:
        bool: True if valid, else False.
    """

    return bool(question and question.strip())


if __name__ == "__main__":

    url = "https://www.youtube.com/watch?v=90lLQVZe2Nc"

    print("Video ID:", extract_video_id(url))

    print(clean_text("   Hello     World   "))