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
python ..\..\main.py process-questions --config max_nst_o3m

# Or using pipeline.py directly (uncomment methods in the file)
python .\src\pipeline.py
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

1. **PDF Parsing** (`src/pdf_parsing.py`)
   - Uses Docling library to parse PDF annual reports
   - Converts PDFs to structured JSON with text, tables, and metadata
   - Supports both sequential and parallel processing

2. **Pipeline Management** (`src/pipeline.py`)
   - Main orchestrator that coordinates the entire RAG pipeline
   - Contains multiple configurations for different processing approaches
   - Handles document processing stages: parsing, merging, chunking, vector DB creation

3. **Data Ingestion** (`src/ingestion.py`)
   - Creates vector databases using FAISS
   - Builds BM25 indexes for traditional keyword-based search

4. **Retrieval** (`src/retrieval.py`)
   - VectorRetriever: Retrieves documents using vector similarity search
   - BM25Retriever: Retrieves documents using keyword matching
   - HybridRetriever: Combines vector and LLM reranking approaches

5. **Question Processing** (`src/questions_processing.py`)
   - Main question answering engine
   - Handles both single-company and comparative questions
   - Manages parallel processing of multiple questions
   - Integrates with various retrieval methods

6. **LLM Integration** (`src/api_requests.py`, `src/prompts.py`)
   - Handles API calls to OpenAI, Gemini, and IBM models
   - Contains structured prompts for different question types
   - Implements retry logic and error handling

7. **Reranking** (`src/reranking.py`)
   - LLM-based reranking of retrieved documents
   - Improves relevance of context provided to answer generation

### Data Flow

1. **PDF Processing Pipeline**:
   - Raw PDFs → Docling parsing → Structured JSON → Merged reports → Chunked documents → Vector databases

2. **Question Answering Pipeline**:
   - Question → Company extraction → Document retrieval → Context formation → LLM answer generation → Response validation

### Key Configurations

Several predefined configurations are available in `src/pipeline.py`:
- `max_nst_o3m`: Best performing config using OpenAI's o3-mini model
- `ibm_llama70b`: Alternative using IBM's Llama 70B model
- `gemini_thinking`: Full context answering with Gemini's large context window

## Important Notes

- This is competition code - it's functional but may have rough edges
- IBM Watson integration won't work (was competition-specific)
- GPU recommended for PDF parsing (significantly faster)
- Requires API keys for OpenAI/Gemini services
- No tests or minimal error handling - use with caution in production