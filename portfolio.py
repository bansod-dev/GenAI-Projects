
import streamlit as st

st.set_page_config(
    page_title="GenAI | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #241044 0%, transparent 38%),
        radial-gradient(ellipse at 95% 25%, #102647 0%, transparent 35%),
        #080a10;
    color: #f4f4fa;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    padding: 65px 0 45px 0;
}

.eyebrow {
    display: inline-block;
    color: #c4b5fd;
    background: #171329;
    border: 1px solid #493276;
    padding: 8px 15px;
    border-radius: 30px;
    font-size: 13px;
    letter-spacing: 1px;
}

.hero h1 {
    font-size: clamp(42px, 7vw, 76px);
    line-height: 1.08;
    letter-spacing: -3px;
    font-weight: 800;
    margin: 25px 0 18px 0;
    color: #ffffff;
}

.gradient-text {
    background: linear-gradient(90deg, #a78bfa, #60a5fa, #5eead4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #aaaabd;
    font-size: 17px;
    line-height: 1.8;
    max-width: 680px;
}

.section-label {
    color: #a78bfa;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 12px;
    font-weight: 700;
}

.section-heading {
    color: #f8fafc;
    font-size: 32px;
    font-weight: 750;
    margin: 8px 0 24px 0;
    letter-spacing: -1px;
}

.project-card {
    background: linear-gradient(145deg, #151522, #0e111b);
    border: 1px solid #29283b;
    border-radius: 20px;
    padding: 27px;
    min-height: 260px;
    margin-bottom: 15px;
    transition: border-color .2s ease, transform .2s ease;
}

.project-card:hover {
    border-color: #8b5cf6;
    transform: translateY(-4px);
}

.project-icon {
    font-size: 30px;
    margin-bottom: 18px;
}

.project-card h3 {
    color: #ffffff;
    font-size: 22px;
    margin: 0 0 12px 0;
}

.project-card p {
    color: #a7a7bc;
    line-height: 1.7;
    font-size: 14px;
    min-height: 72px;
}

.tag {
    display: inline-block;
    background: #211b37;
    color: #c4b5fd;
    padding: 6px 10px;
    border-radius: 7px;
    font-size: 11px;
    margin: 3px 3px 0 0;
}

.info-panel {
    background: linear-gradient(120deg, #171326, #101a2c);
    border: 1px solid #30294b;
    border-radius: 20px;
    padding: 25px;
    margin: 12px 0 28px 0;
}

.metric-number {
    color: #c4b5fd;
    font-size: 27px;
    font-weight: 800;
}

.metric-caption {
    color: #a5a5ba;
    font-size: 12px;
}

.stButton > button, .stLinkButton > a {
    background: linear-gradient(100deg, #7c3aed, #4f46e5);
    color: white !important;
    border: 1px solid #8b5cf6;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: 600;
}

.stButton > button:hover, .stLinkButton > a:hover {
    border-color: #c4b5fd;
    color: white !important;
}

a {
    color: #c4b5fd !important;
}

hr {
    border-color: #272536;
    margin: 35px 0;
}

.footer {
    text-align: center;
    color: #77778f;
    font-size: 12px;
    padding: 30px 0 10px 0;
}
</style>
""", unsafe_allow_html=True)


# Navigation
nav1, nav2 = st.columns([3, 1])

with nav1:
    st.markdown(
        "<span style='font-size:20px;font-weight:800;'>✦ <span "
        "style='color:#a78bfa'>GEN</span>AI.PORTFOLIO</span>",
        unsafe_allow_html=True
    )

with nav2:
    st.link_button(
        "GitHub ↗",
        "https://github.com/bansod-dev/GenAI-Projects",
        use_container_width=True
    )


# Hero section
st.markdown("""
<div class="hero">
    <span class="eyebrow">✦ &nbsp; EXPLORING THE WORLD OF AI</span>
    <h1>Building things<br>with <span class="gradient-text">intelligence.</span></h1>
    <p>
        Hey, I'm an AI &amp; Data Science student exploring Generative AI,
        Large Language Models, and intelligent applications.
        This is where my experiments turn into projects.
    </p>
</div>
""", unsafe_allow_html=True)

st.link_button(
    "Explore my projects ↓",
    "https://github.com/bansod-dev/GenAI-Projects"
)

st.markdown("""
<div class="info-panel">
  <div class="section-label">CURRENT FOCUS</div>
  <div style="font-size:20px;font-weight:700;margin:10px 0;">
    Generative AI · LLM Applications · Intelligent Systems
  </div>
  <div style="color:#a7a7bc;font-size:14px;">
    Learning by building, experimenting, and shipping projects.
  </div>
</div>
""", unsafe_allow_html=True)


# Projects
st.markdown('<div class="section-label">SELECTED WORK</div>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Projects that I\'ve built.</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="project-card">
        <div class="project-icon">🎬</div>
        <h3>CineSage</h3>
        <p>
            An LLM-powered movie information application exploring
            prompt templates, structured outputs, and LangChain.
        </p>
        <span class="tag">LANGCHAIN</span>
        <span class="tag">GROQ</span>
        <span class="tag">PYDANTIC</span>
        <span class="tag">STREAMLIT</span>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Explore CineSage ↗",
        "https://github.com/bansod-dev/GenAI-Projects/tree/main/CineSage",
        use_container_width=True
    )

with col2:
    st.markdown("""
    <div class="project-card">
        <div class="project-icon">🤖</div>
        <h3>AI Assistant Chatbot</h3>
        <p>
            Conversational AI experiments exploring different language
            models, chatbot personalities, and interactive interfaces.
        </p>
        <span class="tag">PYTHON</span>
        <span class="tag">GROQ</span>
        <span class="tag">HUGGING FACE</span>
        <span class="tag">LLMs</span>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Explore Chat Models ↗",
        "https://github.com/bansod-dev/GenAI-Projects/tree/main/chatmodels",
        use_container_width=True
    )

col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("""
    <div class="project-card">
        <div class="project-icon">🧠</div>
        <h3>Text Embeddings</h3>
        <p>
            An experiment converting text into numerical vector
            representations using a sentence-transformer model.
        </p>
        <span class="tag">EMBEDDINGS</span>
        <span class="tag">HUGGING FACE</span>
        <span class="tag">LANGCHAIN</span>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Explore Embeddings ↗",
        "https://github.com/bansod-dev/GenAI-Projects/tree/main/embeddingmodels",
        use_container_width=True
    )

with col4:
    st.markdown("""
    <div class="project-card">
        <div class="project-icon">⚡</div>
        <h3>LLM Experiments</h3>
        <p>
            A collection of experiments with chat models, local inference,
            and Hugging Face integrations as I explore the LLM ecosystem.
        </p>
        <span class="tag">LLMs</span>
        <span class="tag">PYTHON</span>
        <span class="tag">MODEL EXPLORATION</span>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "View all experiments ↗",
        "https://github.com/bansod-dev/GenAI-Projects/tree/main/chatmodels",
        use_container_width=True
    )


# Tech stack
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown('<div class="section-label">MY TOOLKIT</div>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Tools I work with.</div>',
            unsafe_allow_html=True)

st.markdown("""
<div style="line-height:2.8;">
  <span class="tag">PYTHON</span>
  <span class="tag">LANGCHAIN</span>
  <span class="tag">GROQ</span>
  <span class="tag">HUGGING FACE</span>
  <span class="tag">STREAMLIT</span>
  <span class="tag">PYDANTIC</span>
  <span class="tag">GIT</span>
  <span class="tag">GITHUB</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    DESIGNED WITH PYTHON &nbsp;·&nbsp; POWERED BY CURIOSITY<br><br>
    © 2026 · GenAI Portfolio
</div>
""", unsafe_allow_html=True)
