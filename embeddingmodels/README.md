\# Embedding Models



\## Overview



This folder contains experiments with text embeddings using Hugging Face models and LangChain.



\## Text Embeddings



The `embidding.py` script uses the `sentence-transformers/all-MiniLM-L6-v2` model to convert text into a numerical vector representation.



\### Features



\- Generates embeddings from text.

\- Uses Hugging Face sentence-transformer models.

\- Integrates with LangChain's Hugging Face embeddings.

\- Prints the generated vector and its dimensions.



\## Technologies Used



\- Python

\- LangChain

\- Hugging Face

\- Sentence Transformers



\## Project Structure



```text

embeddingmodels/

└── embidding.py

```



\## Purpose



This experiment explores how text can be represented numerically for applications such as semantic search, document retrieval, and Retrieval-Augmented Generation (RAG).

