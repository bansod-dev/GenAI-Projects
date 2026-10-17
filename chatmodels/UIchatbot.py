
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

# -----------------------------------------
# Page Configuration
# -----------------------------------------
st.set_page_config(
    page_title="Dark AI | Assistant",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------
# Dark AI Styling
# -----------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background:
            radial-gradient(ellipse at 50% 0%, rgba(108, 54, 210, 0.15), transparent 45%),
            #09090f;
        color: #f4f0ff;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }

    .brand {
        text-align: center;
        color: #a78bfa;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 5px;
        margin-bottom: 12px;
    }

    .subtitle {
        text-align: center;
        color: #9290a5;
        font-size: 14px;
        margin-top: -5px;
        margin-bottom: 30px;
    }

    .stSelectbox label {
        color: #c4b5fd !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #14131d;
        border: 1px solid #302644;
        border-radius: 12px;
        color: #f4f0ff;
    }

    [data-testid="stChatMessage"] {
        background: rgba(21, 19, 32, 0.85);
        border: 1px solid rgba(139, 92, 246, 0.15);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 14px;
    }

    [data-testid="stChatMessage"]:hover {
        border-color: rgba(139, 92, 246, 0.4);
    }

    [data-testid="stChatInput"] {
        border: 1px solid #49346c;
        border-radius: 18px;
        background: #13111c;
        box-shadow: 0 0 25px rgba(124, 58, 237, 0.08);
    }

    [data-testid="stChatInput"]:focus-within {
        border-color: #8b5cf6;
        box-shadow: 0 0 25px rgba(124, 58, 237, 0.18);
    }

    [data-testid="stChatInput"] textarea {
        color: #f4f0ff !important;
    }

    .stButton button {
        background: linear-gradient(135deg, #7c3aed, #5b21b6);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
    }

    .stButton button:hover {
        border: 1px solid #a78bfa;
        color: white;
        box-shadow: 0 0 20px rgba(139, 92, 246, 0.2);
    }

    hr {
        border-color: #242031;
    }

    .footer-note {
        text-align: center;
        color: #686579;
        font-size: 12px;
        margin-top: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------
# Header
# -----------------------------------------
st.markdown(
    '<div class="brand">✦ DARK AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align:center; font-size:46px; "
    "font-weight:800; letter-spacing:-1.5px; "
    "color:#f4f0ff; margin-bottom:12px;'>"
    "Your thoughts.<br>Amplified by AI.</h1>",
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A space for your thoughts, powered by intelligence.'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------------------
# Model Configuration
# -----------------------------------------
@st.cache_resource
def get_model():
    return ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7
    )


try:
    model = get_model()
except Exception as e:
    st.error(f"Could not initialize the AI model: {e}")
    st.stop()

# -----------------------------------------
# Assistant Modes
# -----------------------------------------
mode_prompts = {
    "Calm": (
        "You are a calm, thoughtful and supportive AI assistant. "
        "Explain things clearly and respond in a composed, friendly manner."
    ),
    "Funny": (
        "You are a witty, funny AI assistant. Use clever humor, "
        "playful responses and natural conversational language. "
        "Stay helpful and respectful."
    ),
    "Angry": (
        "You are a bold, sarcastic and dramatically expressive AI assistant. "
        "Use playful sass and sharp wit without being genuinely cruel "
        "or insulting the user."
    )
}

col1, col2 = st.columns([3, 1])

with col1:
    selected_mode = st.selectbox(
        "✦ Choose your assistant personality",
        ["Calm", "Funny", "Angry"],
        index=0
    )

with col2:
    st.markdown(
        "<div style='height: 29px'></div>",
        unsafe_allow_html=True
    )

    if st.button("＋ New Chat", use_container_width=True):
        st.session_state.message_history = []
        st.session_state.active_mode = selected_mode
        st.rerun()


# -----------------------------------------
# Chat Session
# -----------------------------------------
if "message_history" not in st.session_state:
    st.session_state.message_history = []

if "active_mode" not in st.session_state:
    st.session_state.active_mode = selected_mode

# Update personality without clearing conversation history
if st.session_state.active_mode != selected_mode:
    st.session_state.active_mode = selected_mode

# -----------------------------------------
# Streaming Helper
# -----------------------------------------
def stream_response(messages):
    """Yield text chunks from the Groq model."""
    for chunk in model.stream(messages):
        content = chunk.content

        if isinstance(content, str):
            if content:
                yield content

        elif isinstance(content, list):
            for item in content:
                if isinstance(item, str):
                    if item:
                        yield item

                elif isinstance(item, dict):
                    if item.get("type") == "text":
                        text_content = item.get("text", "")
                        if text_content:
                            yield text_content

# -----------------------------------------
# Display Chat History
# -----------------------------------------
for message in st.session_state.message_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)

# -----------------------------------------
# Chat Input and Response
# -----------------------------------------
user_input = st.chat_input("Tell me what's on your mind...")

if user_input:
    # Display and save the user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.message_history.append(
        HumanMessage(content=user_input)
    )

    # Include personality instructions
    messages = [
        SystemMessage(content=mode_prompts[selected_mode])
    ] + st.session_state.message_history

    # Generate and display the assistant response
    with st.chat_message("assistant", avatar="🤖"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            with st.spinner("Connecting to Dark AI..."):
                for chunk in stream_response(messages):
                    full_response += chunk
                    response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(
                full_response if full_response else
                "The model returned an empty response."
            )

            # Save only a completed response
            if full_response.strip():
                st.session_state.message_history.append(
                    AIMessage(content=full_response)
                )

        except Exception as e:
            if full_response:
                response_placeholder.markdown(full_response)

            st.error("Dark AI could not complete your request.")
            st.exception(e)

# -----------------------------------------
# Footer
# -----------------------------------------
st.markdown(
    '<div class="footer-note">'
    'DARK AI · Your thoughts, amplified by AI.'
    '</div>',
    unsafe_allow_html=True
)
