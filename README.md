# RAG Challenge Winner Solution

**Read more about this project:**
- Russian: https://habr.com/ru/articles/893356/
- English: https://abdullin.com/ilya/how-to-build-best-rag/

This repository contains the winning solution for both prize nominations in the RAG Challenge competition. The system achieved state-of-the-art results in answering questions about company annual reports using a combination of:

- Custom PDF parsing with Docling
- Vector search with parent document retrieval
- LLM reranking for improved context relevance
- Structured output prompting with chain-of-thought reasoning
- Query routing for multi-company comparisons

## New Features and Improvements

### Enhanced Pipeline Configuration
The pipeline has been significantly enhanced with more configurable options:
- Support for multiple LLM providers (OpenAI, IBM WatsonX, Google Gemini)
- Configurable reranking with sample size and top-N retrieval parameters
- Full context mode for models with large context windows
- Parent document retrieval for better context preservation
- Table serialization for improved handling of tabular data

### Multi-Provider LLM Support
- Full support for OpenAI models including o3-mini
- IBM WatsonX integration with Llama models (70B and 8B)
- Google Gemini integration with both standard and "thinking" models
- Automatic response parsing and validation with schema enforcement

### Advanced Question Processing
- Improved comparative question handling with automatic rephrasing
- Reference validation to prevent hallucinated page references
- Better error handling and debugging capabilities
- Structured output with detailed reasoning process

### Performance Optimizations
- Parallel processing for PDF parsing and table serialization
- Configurable chunk sizes and worker counts for optimal performance
- BM25 database support in addition to vector databases
- Enhanced token management for large context models

### Enhanced PDF Parsing
The PDF parsing module has been significantly improved with:
- Updated to use DoclingParseV4DocumentBackend for better parsing accuracy
- Support for sequential page numbering with gap filling for missing pages
- Enhanced `OCR` capabilities with `EasyOCR` integration
- Improved table structure recognition with cell matching
- Picture extraction and processing capabilities
- Parallel processing of PDF files with configurable chunk sizes
- Better metadata handling with support for both old and new CSV formats
- Debug data export functionality for troubleshooting

## Disclaimer

This is competition code - it's scrappy but it works. Some notes before you dive in:

- IBM Watson integration won't work (it was competition-specific)
- The code might have rough edges and weird workarounds
- No tests, minimal error handling - you've been warned
- You'll need your own API keys for OpenAI/Gemini
- GPU helps a lot with PDF parsing (I used 4090)

If you're looking for production-ready code, this isn't it. But if you want to explore different RAG techniques and their implementations - check it out!

## Quick Start

Clone and setup:
```bash
git clone https://github.com/IlyaRice/RAG-Challenge-2.git
cd RAG-Challenge-2
python -m venv venv
venv\Scripts\Activate.ps1  # Windows (PowerShell)
pip install -e . -r requirements.txt
```

Rename `env` to `.env` and add your API keys.

## Test Dataset

The repository includes two datasets:

1. A small test set (in `data/test_set/`) with 5 annual reports and questions
2. The full ERC2 competition dataset (in `data/erc2_set/`) with all competition questions and reports

Each dataset directory contains its own README with specific setup instructions and available files. You can use either dataset to:

- Study example questions, reports, and system outputs
- Run the pipeline from scratch using provided PDFs
- Use pre-processed data to skip directly to specific pipeline stages

See the respective README files for detailed dataset contents and setup instructions:
- `data/test_set/README.md` - For the small test dataset
- `data/erc2_set/README.md` - For the full competition dataset

## Usage

You can run any part of pipeline by uncommenting the method you want to run in `src/pipeline.py` and executing:
```bash
python .\src\pipeline.py
```

You can also run any pipeline stage using `main.py`, but you need to run it from the directory containing your data:
```bash
cd .\data\test_set\
python ..\..\main.py process-questions --config max_nst_o3m
```

### CLI Commands

Get help on available commands:
```bash
python main.py --help
```

Available commands:
- `download-models` - Download required docling models
- `parse-pdfs` - Parse PDF reports with parallel processing options
- `serialize-tables` - Process tables in parsed reports
- `process-reports` - Run the full pipeline on parsed reports
- `process-questions` - Process questions using specified config

Each command has its own options. For example:
```bash
python main.py parse-pdfs --help
# Shows options like --parallel/--sequential, --chunk-size, --max-workers

python main.py process-reports --config ser_tab
# Process reports with serialized tables config
```

## Configuration Options

The system supports multiple configurations for different use cases:

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

Check `pipeline.py` for more configs and details on them.

## License

MIT