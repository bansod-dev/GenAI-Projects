# CineSage — Movie Information Extractor

CineSage is a Generative AI project that extracts useful information from movie-related paragraphs using LangChain and a Groq-hosted language model.

The project explores two approaches to information extraction: prompt-based text generation and structured output using Pydantic.

## Features

- Extracts movie information from user-provided paragraphs.
- Identifies details such as title, director, release year, genre, cast, plot, setting, themes, and music composer.
- Uses LangChain prompt templates to guide the model.
- Supports structured output using a Pydantic model.
- Includes Streamlit-based interfaces for interacting with the extraction workflows.

## Implementations

### 1. Core Extraction

**File:** `core.py`

Uses `PromptTemplate` to instruct the language model to extract movie information into a predefined, human-readable format.

### 2. Structured Extraction

**File:** `structured.py`

Uses `ChatPromptTemplate`, a Pydantic `MovieInfo` model, and `PydanticOutputParser` to parse the model's response into structured movie data.

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

1. Install the dependencies from the repository's root `requirements.txt`.
2. Create a `.env` file in the repository root.
3. Add your Groq API key:

```text
GROQ_API_KEY=your_groq_api_key
```

Keep your API key private and never commit your `.env` file.

## Run the Applications

Run these commands from the repository root.

**Core extraction — terminal version**

```bash
python CineSage/core.py
```

**Structured extraction — terminal version**

```bash
python CineSage/structured.py
```

**Core extraction — Streamlit interface**

```bash
streamlit run CineSage/UIcore.py
```

**Structured extraction — Streamlit interface**

```bash
streamlit run CineSage/UIstructured.py
```

## Notes

- The language model extracts information from the paragraph supplied by the user.
- Results depend on the input text and model response; verify important information independently.
- The configured model must be available through your Groq account.
- Structured extraction expects the model response to conform to the defined Pydantic schema.

## Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist