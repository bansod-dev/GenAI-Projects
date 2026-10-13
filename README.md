# Generative AI Projects

A collection of my Generative AI projects and experiments built while learning about Large Language Models (LLMs), LangChain, prompt engineering, structured outputs, chatbots, and Hugging Face.

## Projects

### 1. CineSage

A project exploring LLM-powered applications using LangChain.

**What's included:**
- Core LLM interaction
- Prompt templates
- Structured output with Pydantic
- Streamlit interfaces

**Files:** `CineSage/`

### 2. Chat Models

Experiments with conversational AI and different model integrations.

**What's included:**
- Chatbot implementations
- Groq model integration
- Hugging Face model experiments
- Streamlit chatbot interface

**Files:** `chatmodels/`

### 3. Embedding Models

Experiments with text embedding models using Hugging Face integrations.

**Files:** `embeddingmodels/`

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
│   └── UIstructured.py
├── chatmodels/
│   ├── chat.py
│   ├── chatbot.py
│   ├── UIchatbot.py
│   ├── hugingface.py
│   └── localmodel.py
├── embeddingmodels/
│   └── embidding.py
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