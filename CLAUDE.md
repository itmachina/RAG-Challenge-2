# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the winning solution for the RAG Challenge competition. It's a Retrieval-Augmented Generation (RAG) system designed to answer questions about company annual reports using a combination of:

- Custom PDF parsing with Docling
- Vector search with parent document retrieval
- LLM reranking for improved context relevance
- Structured output prompting with chain-of-thought reasoning
- Query routing for multi-company comparisons

## Common Development Commands

### Setup and Installation
```bash
# Clone and setup
git clone https://github.com/IlyaRice/RAG-Challenge-2.git
cd RAG-Challenge-2
python -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Install dependencies
pip install -e . -r requirements.txt

# Rename `env` to `.env` and add your API keys
```

### Running the Pipeline

The system can be run using either the main.py CLI or by directly executing pipeline methods:

```bash
# Using main.py CLI (run from directory containing your data)
cd .\data\test_set\
rag-pipeline process-questions --config max_nst_o3m

# Or using pipeline.py directly (uncomment methods in the file)
python .\rag_challenge\pipeline.py
```


### CLI Commands
```bash
# Get help on available commands
python main.py --help

# Available commands:
python main.py download-models          # Download required docling models
python main.py parse-pdfs               # Parse PDF reports with parallel processing options
python main.py serialize-tables         # Process tables in parsed reports
python main.py process-reports          # Run the full pipeline on parsed reports
python main.py process-questions        # Process questions using specified config
```

## Code Architecture and Structure

### Core Components

1. **PDF Parsing** (`rag_challenge/pdf_parsing.py`)
   - Uses Docling library to parse PDF annual reports
   - Converts PDFs to structured JSON with text, tables, and metadata
   - Supports both sequential and parallel processing

2. **Pipeline Management** (`rag_challenge/pipeline.py`)
   - Main orchestrator that coordinates the entire RAG pipeline
   - Contains multiple configurations for different processing approaches
   - Handles document processing stages: parsing, merging, chunking, vector DB creation

3. **Data Ingestion** (`rag_challenge/ingestion.py`)
   - Creates vector databases using FAISS
   - Builds BM25 indexes for traditional keyword-based search

4. **Retrieval** (`rag_challenge/retrieval.py`)
   - VectorRetriever: Retrieves documents using vector similarity search
   - BM25Retriever: Retrieves documents using keyword matching
   - HybridRetriever: Combines vector and LLM reranking approaches

5. **Question Processing** (`rag_challenge/questions_processing.py`)
   - Main question answering engine
   - Handles both single-company and comparative questions
   - Manages parallel processing of multiple questions
   - Integrates with various retrieval methods

6. **LLM Integration** (`rag_challenge/api_requests.py`, `rag_challenge/prompts.py`)
   - Handles API calls to OpenAI, Gemini, and IBM models
   - Contains structured prompts for different question types
   - Implements retry logic and error handling

7. **Reranking** (`rag_challenge/reranking.py`)
   - LLM-based reranking of retrieved documents
   - Improves relevance of context provided to answer generation

### Data Flow

1. **PDF Processing Pipeline**:
   - Raw PDFs → Docling parsing → Structured JSON → Merged reports → Chunked documents → Vector databases

2. **Question Answering Pipeline**:
   - Question → Company extraction → Document retrieval → Context formation → LLM answer generation → Response validation

### Configuration Options

Several predefined configurations are available in `rag_challenge/pipeline.py`:

- `base` - Basic configuration with minimal features
- `pdr` - Parent document retrieval enabled
- `max` - Full-featured configuration with table serialization
- `max_no_ser_tab` - Full features without table serialization
- `max_nst_o3m` - Best performing config using OpenAI's o3-mini model
- `max_st_o3m` - With table serialization using o3-mini
- `ibm_llama70b` - Alternative using IBM's Llama 70B model
- `ibm_llama8b` - Alternative using IBM's Llama 8B model
- `gemini_thinking` - Full context answering with using enormous context window of Gemini
- `gemini_flash` - Using Gemini Flash model with full context

For advanced configurations with increased retrieval parameters:
- `max_nst_o3m_bc` - Increased top-N and reranking sample size with o3-mini
- `ibm_llama70b_bc` - Increased parameters with IBM Llama 70B
- `gemini_thinking_bc` - Increased top-N with Gemini thinking model

## Important Notes

- This is competition code - it's functional but may have rough edges
- IBM Watson integration won't work (was competition-specific)
- GPU recommended for PDF parsing (significantly faster)
- Requires API keys for OpenAI/Gemini services
- No tests or minimal error handling - use with caution in production

## Troubleshooting

### PDF Parsing Issues

If you encounter issues with PDF parsing, particularly with OCR-related errors, you may need to:

1. Install the required OCR packages:
   ```bash
   pip install rapidocr onnxruntime
   ```

2. If you get DLL load errors on Windows, you may need to install Microsoft Visual C++ Redistributable packages.


### Virtual Environment

The virtual environment for this project is located in the `venv` directory. Always activate it before running any commands:
```bash
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```