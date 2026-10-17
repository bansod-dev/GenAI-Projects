# Chat Models — LLM Experiments

A collection of Generative AI experiments exploring conversational language models, remote inference, local model pipelines, and interactive chatbot interfaces.

🚀 **[Try Dark AI — Live Demo](https://genai-projects-7h4xdkfzfwszvegopj6g3t.streamlit.app/)**

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

An interactive AI chatbot featuring a custom dark-themed Streamlit interface and Groq-powered conversational responses.

**Features:**
- **AI Personalities:** Calm, Funny, and Angry modes.
- **Streaming Responses:** Displays AI responses as they are generated.
- **Conversation History:** Preserves the conversation when switching personalities.
- **New Chat:** Starts a fresh conversation whenever needed.

**Tech Stack:** Python, Streamlit, LangChain, and Groq.

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

Configure the credentials required by the model you want to use before running it.

For Groq-based experiments, create a `.env` file in the repository root:

```env
GROQ_API_KEY=your_groq_api_key
```

Configure a Hugging Face token if required by the selected endpoint or model.

**Security:** Never commit API keys, access tokens, or other secrets to GitHub. Keep your `.env` file excluded from version control.

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
