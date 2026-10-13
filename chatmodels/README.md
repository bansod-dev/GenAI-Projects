# Chat Models — LLM Experiments

A collection of Generative AI experiments exploring conversational models using LangChain, Groq, Hugging Face, and Streamlit.

## Projects

### 1. Basic Groq Chat

**File:** `chat.py`

A simple LangChain experiment that sends a prompt to a Groq-hosted language model and prints its response.

### 2. AI Assistant Chatbot

**File:** `chatbot.py`

An interactive Streamlit chatbot with three AI personality modes:

- **Angry Mode:** Uses playful sarcasm while aiming to provide useful answers.
- **Calm Mode:** Focuses on polite, patient, easy-to-understand explanations.
- **Funny Mode:** Uses humor and a playful tone while answering questions.

The chatbot uses LangChain message objects to maintain conversation history during the session.

### 3. Hugging Face Endpoint

**File:** `hugingface.py`

Experiments with remote model inference using `HuggingFaceEndpoint` and `ChatHuggingFace`. The script is configured to query `deepseek-ai/DeepSeek-R1`.

### 4. Local Hugging Face Pipeline

**File:** `localmodel.py`

Uses `HuggingFacePipeline` with `ChatHuggingFace` to run a text-generation model locally. The configured model is `Qwen/Qwen2.5-0.5B-Instruct`.

### 5. Additional Chatbot Interface

**File:** `UIchatbot.py`

An additional chatbot implementation with a Streamlit interface.

## Tech Stack

- Python
- LangChain
- LangChain Groq
- LangChain Hugging Face
- Streamlit
- Python-dotenv
- Hugging Face models

## Setup

1. Install the dependencies from the repository's root `requirements.txt`.
2. Configure the environment variables required by the model you want to use.
3. For Groq, create a `.env` file in the repository root containing:

```text
GROQ_API_KEY=your_groq_api_key
```

4. For Hugging Face endpoint access, configure your Hugging Face token if required by the selected model.

**Security:** Never commit API keys or tokens to GitHub.

## Run the Scripts

Run these commands from the repository root.

**Basic Groq chat**

```bash
python chatmodels/chat.py
```

**Streamlit chatbot**

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

**Additional Streamlit chatbot interface**

```bash
streamlit run chatmodels/UIchatbot.py
```

## Notes

- Remote inference requires network access and any necessary credentials.
- Local inference may download model files and requires sufficient system resources.
- The Hugging Face endpoint script currently uses a machine-specific `.env` path. Update that path for your own environment if necessary.
- Model availability and access requirements can change.

## Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist