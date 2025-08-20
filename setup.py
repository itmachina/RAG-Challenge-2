from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rag-challenge-2",
    version="1.0.0",
    author="Ilya Abdullin",
    author_email="",
    description="A Retrieval-Augmented Generation (RAG) system for processing PDF documents and answering questions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IlyaRice/RAG-Challenge-2",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "aiohttp==3.10.10",
        "tiktoken==0.8.0",
        "python-dotenv==1.0.1",
        "pydantic==2.9.2",
        "openai==1.51.2",
        "requests==2.32.3",
        "tqdm==4.66.5",
        "rank-bm25==0.2.2",
        "tabulate==0.9.0",
        "docling==2.28.4",
        "pyprojroot==0.3.0",
        "PyPDF2==3.0.1",
        "pandas==2.2.3",
        "faiss-cpu==1.9.0.post1",
        "langchain==0.3.3",
        "json_repair==0.35.0",
        "google-ai-generativelanguage==0.6.15",
        "google-api-core==2.24.1",
        "google-api-python-client==2.160.0",
        "google-auth==2.38.0",
        "google-auth-httplib2==0.2.0",
        "google-generativeai==0.8.4",
        "googleapis-common-protos==1.66.0",
        "click==8.1.7",
        "httpx==0.27.2"
    ],
    entry_points={
        "console_scripts": [
            "rag-pipeline=rag_challenge.cli:main",
        ],
    },
    include_package_data=True,
)