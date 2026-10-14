# Generative AI Projects

A collection of Generative AI applications and experiments built while exploring Large Language Models (LLMs), LangChain, prompt engineering, structured outputs, chatbots, and text embeddings.

## Featured Projects

### 1. Dark AI — AI Assistant

A Streamlit-based conversational AI assistant powered by Groq, featuring selectable AI personalities and a dark-themed interface.

**Features**
- Interactive chatbot interface
- Multiple AI personalities: Calm, Funny, and Angry
- Conversational history
- Streaming responses in the chatbot implementation

**Technologies:** Python, Streamlit, LangChain, Groq

**File:** [`portfolio.py`](portfolio.py)

### 2. CineSage — Movie Information Extractor

An LLM-powered application exploring movie information extraction and structured responses using LangChain.

**Features**
- LLM interaction and prompt templates
- Structured outputs using Pydantic
- Streamlit interfaces

**Folder:** [`CineSage/`](CineSage/)

**Documentation:** [`CineSage README`](CineSage/README.md)

### 3. AI Assistant Chatbot Experiments

A collection of conversational AI implementations exploring different language models and chatbot interfaces.

**Features**
- Chatbot implementations
- Groq model integration
- Hugging Face model experiments
- Streamlit chatbot interface

**Folder:** [`chatmodels/`](chatmodels/)

**Documentation:** [`Chat Models README`](chatmodels/README.md)

## Other Experiments

### Text Embeddings

An experiment exploring how sentence-transformer models convert text into numerical vector representations for semantic applications.

**Folder:** [`embeddingmodels/`](embeddingmodels/)

**Documentation:** [`Embedding Models README`](embeddingmodels/README.md)

## Tech Stack

- **Language:** Python
- **LLM Framework:** LangChain
- **Model Providers:** Groq, Hugging Face
- **Interface:** Streamlit
- **Structured Outputs:** Pydantic
- **Configuration:** Python-dotenv
- **Version Control:** Git and GitHub

## Project Structure

```text
GenAI-Projects/
├── CineSage/
├── chatmodels/
├── embeddingmodels/
├── portfolio.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies listed in `requirements.txt`.
4. Configure the API keys required by your chosen project in a local `.env` file.
5. Run the relevant Python or Streamlit entry point.

Check each project's documentation for its specific dependencies, environment variables, and execution instructions.

## Security

- Keep API keys and private credentials out of source code.
- Store secrets in a local `.env` file.
- Ensure `.env` and virtual environment directories are excluded from version control.
- Never publish private API keys or tokens.

## Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist
