# CineSage — Movie Information Extractor

CineSage is a Generative AI project that extracts structured movie information from user-provided text using LangChain and a Groq-hosted language model.

It explores two approaches to information extraction: prompt-based generation and schema-based structured output with Pydantic.

## Features

- Extracts movie information from descriptive paragraphs.
- Identifies the title, director, release year, genre, cast, plot, setting, themes, and music composer.
- Uses LangChain prompt templates to guide extraction.
- Supports structured responses through Pydantic models.
- Provides Streamlit interfaces for interactive use.
- Includes both terminal-based and graphical implementations.

## Implementations

### 1. Core Extraction

**File:** `core.py`

Uses LangChain's `PromptTemplate` to guide the language model in extracting movie details into a predefined, human-readable format.

### 2. Structured Extraction

**File:** `structured.py`

Uses `ChatPromptTemplate`, a Pydantic `MovieInfo` model, and `PydanticOutputParser` to organize the language model's response into a predefined schema.

### Streamlit Interfaces

- `UIcore.py` — Interface for the core extraction workflow.
- `UIstructured.py` — Interface for the structured extraction workflow.

## Tech Stack

- Python
- LangChain
- Groq
- Pydantic
- Streamlit
- Python-dotenv

## Project Structure

```text
CineSage/
├── core.py
├── structured.py
├── UIcore.py
├── UIstructured.py
└── README.md
```

## Setup

1. Install the dependencies listed in the repository's root `requirements.txt`.
2. Create a `.env` file in the repository root.
3. Add your Groq API key:

```text
GROQ_API_KEY=your_groq_api_key
```

**Security:** Keep your API key private. Never commit `.env` files or API credentials to GitHub.

## Run the Applications

Run these commands from the repository root.

**Core extraction — terminal**

```bash
python CineSage/core.py
```

**Structured extraction — terminal**

```bash
python CineSage/structured.py
```

**Core extraction — Streamlit**

```bash
streamlit run CineSage/UIcore.py
```

**Structured extraction — Streamlit**

```bash
streamlit run CineSage/UIstructured.py
```

## Notes

- Extraction results depend on the supplied text and the language model's response.
- Verify important movie information independently, as generated details may be inaccurate.
- The configured model must be accessible through your Groq account.
- Structured extraction relies on the output matching the defined Pydantic schema.

## Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist