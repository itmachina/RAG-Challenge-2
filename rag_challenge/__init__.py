"""
RAG Challenge 2 - A Retrieval-Augmented Generation system for processing PDF documents and answering questions.
"""

__version__ = "1.0.0"
__author__ = "Ilya Abdullin"

# Import main classes for easier access
from .pipeline import Pipeline
from .pdf_parsing import PDFParser
from .questions_processing import QuestionsProcessor

__all__ = [
    "Pipeline",
    "PDFParser", 
    "QuestionsProcessor"
]