# Qwen Code Configuration for RAG-Challenge-2

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) challenge focused on processing PDF documents, extracting information, and answering questions using advanced language models. The project includes components for PDF parsing, document ingestion, retrieval, reranking, and question processing.

## Key Technologies
- Python 3.x
- PyPDF2, pdfplumber for PDF processing
- FAISS for vector storage and similarity search
- Transformers library for language models
- OpenAI API integration
- Custom RAG pipeline implementation

## Directory Structure
- `rag_challenge/`: Main source code for the RAG pipeline as a Python package
- `data/`: Contains datasets, including test sets and ERC2 datasets
- `output/`: Generated outputs like parsed documents and answers
- `pdf_reports/`: Sample PDF documents for processing

## Code Style Guidelines
- Follow PEP 8 for Python code
- Use descriptive variable and function names
- Include docstrings for all functions and classes
- Add comments for complex logic
- Use type hints where possible

## Key Files and Their Functions
- `rag_challenge/pipeline.py`: Main RAG pipeline orchestration
- `rag_challenge/pdf_parsing.py`: PDF document parsing functionality
- `rag_challenge/ingestion.py`: Document ingestion and preprocessing
- `rag_challenge/retrieval.py`: Information retrieval from documents
- `rag_challenge/reranking.py`: Reranking of retrieved results
- `rag_challenge/questions_processing.py`: Question processing and answering
- `rag_challenge/prompts.py`: Prompt templates for language models

## Preferred Approaches
1. When suggesting code changes, provide complete functions/methods rather than fragments
2. Always consider performance implications of changes
3. Prefer modular, reusable code components
4. Use appropriate error handling and logging
5. When working with PDFs, consider both text extraction and table extraction needs
6. For RAG implementations, focus on accuracy and relevance of retrieved information

## Common Tasks
- PDF parsing and text extraction
- Document chunking and embedding
- Vector database operations
- Language model prompt engineering
- Evaluation of retrieval and generation quality

## Important Notes
- The project uses both local processing and API calls to language models
- Be careful with API costs when suggesting extensive testing
- Consider both accuracy and efficiency in RAG pipeline improvements
- Handle various PDF formats and structures gracefully