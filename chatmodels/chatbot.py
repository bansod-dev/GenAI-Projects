import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Assistant Chatbot",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #888888;
        margin-bottom: 30px;
    }

    .mode-box {
        padding: 18px;
        border-radius: 15px;
        background: rgba(128, 128, 128, 0.08);
        margin-bottom: 20px;
    }

    .stChatMessage {
        border-radius: 15px;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------
st.markdown(
    '<div class="title">🤖 AI Assistant Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI assistant, your style.</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Groq model
# -----------------------------
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# -----------------------------
# AI modes
# -----------------------------
modes = {
    "😡 Angry Mode": (
        "You are an angry AI assistant teacher. "
        "You are rude and sarcastic. "
        "You answer questions in an angry and sarcastic manner. "
        "You can use playful sarcasm, but you must still provide useful answers. "
        "Do not make threats or use hateful language."
    ),

    "😌 Calm Mode": (
        "You are a calm AI assistant teacher. "
        "You are polite, respectful, helpful, patient, understanding, "
        "supportive, encouraging, and clear. "
        "Explain concepts in an easy-to-understand manner."
    ),

    "😂 Funny Mode": (
        "You are a funny AI assistant teacher. "
        "You are humorous, witty, playful, energetic, and entertaining. "
        "Use jokes and light humor when appropriate, while still giving "
        "accurate and useful educational answers."
    )
}


# -----------------------------
# Mode selection
# -----------------------------
st.markdown("### 🎭 Choose your AI personality")

selected_mode = st.selectbox(
    "Select a mode",
    list(modes.keys()),
    label_visibility="collapsed"
)


# -----------------------------
# Initialize conversation
# -----------------------------
if "message_history" not in st.session_state:

    st.session_state.message_history = [
        SystemMessage(
            content=(
                "You are my AI assistant.\n\n"
                + modes[selected_mode]
            )
        )
    ]

    st.session_state.selected_mode = selected_mode


# -----------------------------
# Display conversation
# -----------------------------
for message in st.session_state.message_history:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)


# -----------------------------
# Chat input
# -----------------------------
prompt = st.chat_input("Ask your AI teacher something...")


if prompt:

    # Add user message
    st.session_state.message_history.append(
        HumanMessage(content=prompt)
    )

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    response = model.invoke(
        st.session_state.message_history
    )

    # Add AI response
    st.session_state.message_history.append(
        AIMessage(content=response.content)
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.write(response.content)