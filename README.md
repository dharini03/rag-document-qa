# RAG-Based Document Question Answering System

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF and DOCX documents and ask questions based on their content. The system retrieves relevant information from uploaded documents and generates context-based answers using a language generation model.

## Overview

This project demonstrates the implementation of a basic RAG pipeline by combining document processing, text embeddings, vector similarity search and text generation.

The application uses Django as its backend framework, Sentence Transformers to generate text embeddings, FAISS for similarity-based retrieval, and FLAN-T5-base for answer generation.

## Features

- **Document Upload:** Upload PDF and DOCX files.
- **Text Extraction:** Extract document content using PyMuPDF and python-docx.
- **Text Chunking:** Divide extracted text into smaller chunks of approximately 500 characters.
- **Embedding Generation:** Generate 384-dimensional text embeddings using Sentence Transformers.
- **Vector Search:** Use FAISS to perform similarity-based retrieval.
- **Context Retrieval:** Retrieve the top 3 relevant text chunks for a given question.
- **Answer Generation:** Generate answers using Google's FLAN-T5-base model based on the retrieved context.
- **Web Interface:** Interact with uploaded documents through a Django-based interface.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Document Processing | PyMuPDF, python-docx |
| Embedding Model | all-MiniLM-L6-v2 |
| Embedding Library | Sentence Transformers |
| Vector Search | FAISS |
| Text Generation | Hugging Face Transformers |
| Language Model | google/flan-t5-base |
| Database | YugabyteDB (PostgreSQL-compatible) |
| Frontend | HTML, CSS |

## How It Works

The application follows a Retrieval-Augmented Generation workflow:

1. **Document Upload:** The user uploads a PDF or DOCX document.
2. **Text Extraction:** The application extracts text from the uploaded document.
3. **Text Chunking:** Extracted content is divided into smaller chunks of approximately 500 characters.
4. **Embedding Generation:** Sentence Transformers converts each text chunk into a 384-dimensional vector.
5. **Vector Indexing:** The generated embeddings are added to a FAISS vector index.
6. **Question Embedding:** The user's question is converted into an embedding using the same embedding model.
7. **Similarity Search:** FAISS retrieves the top 3 relevant text chunks.
8. **Answer Generation:** The retrieved chunks and user question are passed as context to FLAN-T5-base to generate an answer.

## Architecture

```text
             Document Upload
                    |
                    v
             Text Extraction
                    |
                    v
              Text Chunking
                    |
                    v
           Embedding Generation
                    |
                    v
              FAISS Index
                    |
                    |
User Question ------+
       |
       v
Query Embedding
       |
       v
Similarity Search
       |
       v
Retrieve Top 3 Chunks
       |
       v
Combine Context + Question
       |
       v
     FLAN-T5
       |
       v
  Generated Answer

## Limitations

- Supports PDF and DOCX files containing selectable text.
- Scanned documents requiring OCR are not supported.
- Uses fixed-size text chunking.
- Retrieves a fixed number of relevant chunks (top 3).
- Answer quality depends on the relevance of retrieved content and the generated response.
- Uses a basic retrieval pipeline without hybrid search or reranking.

## Future Enhancements

- Add OCR support for scanned documents.
- Implement semantic text chunking.
- Explore hybrid search and reranking techniques.
- Add source references to generated answers.
- Introduce user authentication and document-level access control.
- Improve retrieval and answer quality.

## Purpose

This project explores the practical implementation of Retrieval-Augmented Generation by integrating document processing, semantic embeddings, vector similarity search and language generation into a web application.
