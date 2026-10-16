# Chat Models — LLM Experiments

A collection of Generative AI experiments exploring conversational language models, remote inference, local model pipelines, and interactive chatbot interfaces.

## Projects

### 1. Basic Groq Chat

**File:** `chat.py`

A simple LangChain experiment that sends prompts to a Groq-hosted language model and displays the response.

### 2. AI Assistant Chatbot

**File:** `chatbot.py`

An interactive Streamlit chatbot experimenting with different AI personality modes:

- **Angry Mode:** Playful sarcasm while aiming to provide useful answers.
- **Calm Mode:** Polite, patient, easy-to-understand explanations.
- **Funny Mode:** Humorous and playful responses.

Uses LangChain message objects to maintain conversation history during the session.

### 3. Hugging Face Endpoint

**File:** `hugingface.py`

Experiments with remote model inference using `HuggingFaceEndpoint` and `ChatHuggingFace`. The configured model is `deepseek-ai/DeepSeek-R1`.

### 4. Local Hugging Face Pipeline

**File:** `localmodel.py`

Experiments with local text generation using `HuggingFacePipeline` and `ChatHuggingFace`. The configured model is `Qwen/Qwen2.5-0.5B-Instruct`.

Local inference depends on available hardware, installed dependencies, and model compatibility.

### 5. Dark AI Chatbot Interface

**File:** `UIchatbot.py`

A Streamlit chatbot experiment featuring a dark-themed interface and Groq-powered conversational responses.

This implementation is separate from the main `portfolio.py` application in the repository root.

## Tech Stack

- Python
- LangChain
- LangChain Groq
- LangChain Hugging Face
- Streamlit
- Python-dotenv
- Hugging Face models

## Setup

Install the dependencies listed in the repository's root `requirements.txt`:

```bash
pip install -r requirements.txt
```

The root requirements file provides the shared environment for these experiments. Some scripts, especially local Hugging Face inference, may require additional model-specific dependencies depending on the installed versions and hardware.

Configure the credentials required by the model you want to use before running it.

For Groq-based experiments, create a `.env` file in the repository root:

```text
GROQ_API_KEY=your_groq_api_key
```

Configure a Hugging Face token if required by the selected endpoint or model.

**Security:** Never commit API keys, access tokens, or other secrets to GitHub.

## Run the Scripts

Run these commands from the repository root.

**Basic Groq chat**

```bash
python chatmodels/chat.py
```

**AI Assistant chatbot**

```bash
streamlit run chatmodels/chatbot.py
```

**Hugging Face endpoint experiment**

```bash
python chatmodels/hugingface.py
```

**Local Hugging Face pipeline**

```bash
python chatmodels/localmodel.py
```

**Dark AI chatbot interface**

```bash
streamlit run chatmodels/UIchatbot.py
```

## Notes

- Remote inference requires network access and may require API credentials.
- Local inference can download model files and requires sufficient system resources.
- Model availability, access permissions, and dependency compatibility may change.
- Keep credentials in environment variables or an ignored `.env` file.

## Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist
