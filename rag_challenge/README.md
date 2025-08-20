# RAG Challenge 2 Python Package

This is a Python package version of the RAG Challenge winner solution, restructured for use as a library in other projects.

## Installation

To install this package, clone the repository and install it in development mode:

```bash
git clone https://github.com/IlyaRice/RAG-Challenge-2.git
cd RAG-Challenge-2
pip install -e .
```

Or install directly from the repository:

```bash
pip install git+https://github.com/IlyaRice/RAG-Challenge-2.git
```

## Usage

### As a Library

You can import and use the main components directly in your Python code:

```python
from rag_challenge import Pipeline, PDFParser, QuestionProcessor

# Initialize the pipeline
pipeline = Pipeline(root_path=Path("/path/to/your/data"))

# Process PDF reports
pipeline.parse_pdf_reports()

# Process questions
pipeline.process_questions()
```

### Command Line Interface

The package also provides a command-line interface:

```bash
# Get help on available commands
rag-pipeline --help

# Parse PDF reports
rag-pipeline parse-pdfs

# Process questions
rag-pipeline process-questions --config max_nst_o3m
```

## Features

- Custom PDF parsing with Docling
- Vector search with parent document retrieval
- LLM reranking for improved context relevance
- Structured output prompting with chain-of-thought reasoning
- Query routing for multi-company comparisons
- Support for multiple LLM providers (OpenAI, IBM WatsonX, Google Gemini)

## Requirements

- Python 3.8 or higher
- See `requirements.txt` for a full list of dependencies