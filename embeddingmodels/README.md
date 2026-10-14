# Text Embeddings — Hugging Face & LangChain

## Overview

This project explores text embeddings using Hugging Face sentence-transformer models and LangChain.

Text embeddings convert text into numerical vectors that capture aspects of its meaning. These representations are useful for comparing text and retrieving semantically similar information.

## Implementation

**File:** `embidding.py`

Uses the `sentence-transformers/all-MiniLM-L6-v2` model to generate numerical representations of text and demonstrates integration with LangChain's Hugging Face embeddings.

## Features

- Generates numerical embeddings from text.
- Uses a pretrained Sentence Transformers model.
- Integrates with LangChain's Hugging Face embeddings.
- Displays the generated vector and its dimensions.
- Introduces concepts used in semantic search and retrieval systems.

## Tech Stack

- Python
- LangChain
- Hugging Face
- Sentence Transformers

## Project Structure

```text
embeddingmodels/
└── embidding.py
```

## Purpose

This experiment provides a foundation for understanding how text can be represented numerically and used in applications such as:

- **Semantic search:** Finding text based on meaning rather than exact keyword matches.
- **Document retrieval:** Identifying relevant documents for a query.
- **Retrieval-Augmented Generation (RAG):** Retrieving relevant context to support an AI model's response.

## Notes

- The script uses a pretrained embedding model.
- Initial execution may download model files.
- The generated vector's dimensions depend on the selected model.

## Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist