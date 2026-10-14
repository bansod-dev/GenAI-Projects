
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Dark AI | Assistant",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Dark AI styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #241044 0%, transparent 38%),
        radial-gradient(ellipse at 95% 20%, #102647 0%, transparent 35%),
        #08090e;
    color: #f4f4fa;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    padding: 22px 0 24px 0;
}

.eyebrow {
    display: inline-block;
    color: #c4b5fd;
    background: #171329;
    border: 1px solid #493276;
    padding: 8px 15px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-title {
    font-size: clamp(38px, 5vw, 62px);
    line-height: 1.12;
    letter-spacing: -2px;
    font-weight: 800;
    margin: 25px 0 15px 0;
    color: #ffffff;
}

.gradient-text {
    background: linear-gradient(90deg, #c4b5fd, #818cf8, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #a3a3b8;
    font-size: 15px;
    line-height: 1.8;
    max-width: 650px;
}

.status-pill {
    display: inline-block;
    border: 1px solid #283d37;
    background: #101b19;
    color: #86efac;
    border-radius: 30px;
    padding: 8px 13px;
    font-size: 12px;
    margin-top: 12px;
}

.section-label {
    color: #a78bfa;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 25px 0 14px 0;
}

/* Personality selector */
div[data-testid="stSelectbox"] label {
    color: #c4b5fd !important;
    font-weight: 600;
}

div[data-testid="stSelectbox"] > div > div {
    background: #12121d;
    border-color: #493276;
    border-radius: 12px;
}

/* Chat messages */
div[data-testid="stChatMessage"] {
    background: rgba(20, 20, 33, 0.85);
    border: 1px solid #29273a;
    border-radius: 16px;
    padding: 16px 18px;
    margin-bottom: 14px;
}

div[data-testid="stChatInput"] {
    border: 1px solid #493276;
    border-radius: 16px;
    background: #11111b;
    box-shadow: 0 0 24px rgba(139, 92, 246, 0.10);
}

div[data-testid="stChatInput"] textarea {
    color: #f4f4fa;
}

.stButton > button {
    background: linear-gradient(100deg, #7c3aed, #4f46e5);
    color: white !important;
    border: 1px solid #8b5cf6;
    border-radius: 10px;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #c4b5fd;
}

hr {
    border-color: #292638;
    margin: 28px 0;
}

.empty-state {
    text-align: center;
    padding: 42px 18px;
    background: rgba(20, 20, 33, 0.55);
    border: 1px solid #29273a;
    border-radius: 18px;
    margin: 15px 0 25px 0;
}

.empty-icon {
    font-size: 35px;
    color: #c4b5fd;
    margin-bottom: 12px;
}

.empty-title {
    font-size: 21px;
    font-weight: 700;
    color: #ffffff;
}

.empty-subtitle {
    color: #9696ad;
    font-size: 14px;
    margin-top: 10px;
}

.footer {
    text-align: center;
    color: #73738a;
    font-size: 11px;
    padding-top: 25px;
    letter-spacing: 1px;
}

@media (max-width: 640px) {
    .block-container {
        padding: 1rem 1rem 5rem 1rem;
    }

    .hero-title {
        letter-spacing: -1px;
    }
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header — HTML rendered correctly
# -----------------------------
st.markdown("""
<div class="hero">
    <span class="eyebrow">✦ &nbsp; INTELLIGENT CONVERSATION</span>

    <div class="hero-title">
        Your thoughts.<br>
        <span class="gradient-text">Amplified by AI.</span>
    </div>

    <div class="hero-subtitle">
        Your personal AI assistant for learning, exploring,
        and thinking through ideas.
    </div>

    <div class="status-pill">● &nbsp; AI ASSISTANT</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# -----------------------------
# Groq model
# -----------------------------
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# -----------------------------
# AI personalities
# -----------------------------
modes = {
    "😡 Angry Mode": (
        "You are an angry AI assistant teacher. "
        "Use playful sarcasm and an angry tone, but remain helpful. "
        "Do not use threats or hateful language."
    ),
    "😌 Calm Mode": (
        "You are a calm AI assistant teacher. "
        "Be polite, respectful, patient, supportive, and clear. "
        "Explain concepts simply."
    ),
    "😂 Funny Mode": (
        "You are a funny AI assistant teacher. "
        "Be witty, playful, and entertaining while providing "
        "accurate and useful answers."
    )
}


# -----------------------------
# Session state
# -----------------------------
if "message_history" not in st.session_state:
    st.session_state.message_history = []

if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = "😌 Calm Mode"


# -----------------------------
# Personality selector
# -----------------------------
st.markdown(
    '<div class="section-label">01 / CHOOSE YOUR PERSONALITY</div>',
    unsafe_allow_html=True
)

selected_mode = st.selectbox(
    "AI personality",
    options=list(modes.keys()),
    index=list(modes.keys()).index(
        st.session_state.selected_mode
    ),
    label_visibility="collapsed"
)

st.session_state.selected_mode = selected_mode


# -----------------------------
# Conversation
# -----------------------------
st.markdown(
    '<div class="section-label">02 / YOUR CONVERSATION</div>',
    unsafe_allow_html=True
)

if not st.session_state.message_history:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">✦</div>
        <div class="empty-title">Start a conversation</div>
        <div class="empty-subtitle">
            Ask a question, explore an idea, or learn something new.
        </div>
    </div>
    """, unsafe_allow_html=True)


# Display previous messages
for message in st.session_state.message_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.write(message.content)


# -----------------------------
# Chat input and response
# -----------------------------
prompt = st.chat_input("Message your AI assistant...")

if prompt:
    user_message = HumanMessage(content=prompt)
    st.session_state.message_history.append(user_message)

    with st.chat_message("user"):
        st.write(prompt)

    conversation = [
        SystemMessage(content=modes[st.session_state.selected_mode]),
        *st.session_state.message_history
    ]

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            try:
                response = model.invoke(conversation)
                st.write(response.content)

                st.session_state.message_history.append(
                    AIMessage(content=response.content)
                )

            except Exception as error:
                st.error(f"Could not generate a response: {error}")


# -----------------------------
# Footer
# -----------------------------
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    BUILT WITH PYTHON &nbsp;·&nbsp; POWERED BY AI<br><br>
    DARK AI · 2026
</div>
""", unsafe_allow_html=True)
