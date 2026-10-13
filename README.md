# Generative AI Projects

A collection of my Generative AI projects and experiments built while learning about Large Language Models (LLMs), LangChain, prompt engineering, structured outputs, chatbots, and Hugging Face.

## Featured Projects

### 1. CineSage — Movie Information Extractor

An LLM-powered application exploring movie information extraction using LangChain.

**What's included:**
- Core LLM interaction
- Prompt templates
- Structured output with Pydantic
- Streamlit interfaces

**Folder:** [`CineSage/`](CineSage/)

**Documentation:** [CineSage README](CineSage/README.md)

### 2. AI Assistant Chatbot

A collection of conversational AI implementations exploring different language models and chatbot interfaces.

**What's included:**
- Chatbot implementations
- Groq model integration
- Hugging Face model experiments
- Streamlit chatbot interface

**Folder:** [`chatmodels/`](chatmodels/)

**Documentation:** [Chat Models README](chatmodels/README.md)

## Experiments

### Embedding Models

A learning experiment using Hugging Face sentence-transformer models to convert text into numerical vector representations.

**Folder:** [`embeddingmodels/`](embeddingmodels/)

**Documentation:** [Embedding Models README](embeddingmodels/README.md)

## Tech Stack

- Python
- LangChain
- Groq
- Hugging Face
- Streamlit
- Pydantic
- Python-dotenv

## Project Structure

```text
GenAI-Projects/
├── CineSage/
│   ├── core.py
│   ├── structured.py
│   ├── UIcore.py
│   ├── UIstructured.py
│   └── README.md
├── chatmodels/
│   ├── chat.py
│   ├── chatbot.py
│   ├── UIchatbot.py
│   ├── hugingface.py
│   ├── localmodel.py
│   └── README.md
├── embeddingmodels/
│   ├── embidding.py
│   └── README.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

1. Clone this repository.
2. Install the dependencies listed in `requirements.txt`.
3. Create a `.env` file in the project root and add the API keys required by the specific project.
4. Run the relevant Python or Streamlit file for the project you want to explore.

**Note:** Required API keys, model access, and package versions may vary by project. Check the individual files before running them.

## Security

API keys and environment files are excluded from version control. Never commit secrets or private credentials.

## Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist