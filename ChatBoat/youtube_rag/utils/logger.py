"""
logger.py

Centralized logging configuration for the RAG project.
"""

import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.

    Args:
        name (str): Usually pass __name__

    Returns:
        logging.Logger
    """
    return logging.getLogger(name)