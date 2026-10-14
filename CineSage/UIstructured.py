
import os
from typing import List, Optional

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

# --------------------------------------------------
# Configuration
# --------------------------------------------------
load_dotenv()

# Streamlit Cloud secrets support; local .env still works.
try:
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

st.set_page_config(
    page_title="CineSage | Movie Intelligence",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# Styling — matches the dark portfolio aesthetic
# --------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --background: #0b0b10;
        --surface: #13131c;
        --border: #282638;
        --purple: #a78bfa;
        --purple-bright: #8b5cf6;
        --muted: #a3a3b5;
        --text: #f4f2ff;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 50% -15%, #282044 0%, transparent 48%),
            var(--background);
        color: var(--text);
        font-family: 'DM Sans', sans-serif;
    }

    h1, h2, h3, .brand, .eyebrow {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    .block-container {
        max-width: 1120px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    .brand {
        color: var(--text);
        font-size: 1.05rem;
        font-weight: 700;
        letter-spacing: -0.4px;
    }

    .brand span {
        color: var(--purple);
    }

    .eyebrow {
        color: var(--purple);
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 2.2px;
        text-transform: uppercase;
    }

    .hero-title {
        color: var(--text);
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2.5rem, 6vw, 4.4rem);
        font-weight: 700;
        letter-spacing: -2.8px;
        line-height: 1.08;
        margin: 0.7rem 0 1rem;
    }

    .hero-title span {
        color: var(--purple);
    }

    .hero-copy {
        color: var(--muted);
        font-size: 1.05rem;
        line-height: 1.8;
        max-width: 690px;
    }

    .section-label {
        color: var(--purple);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1.6px;
        text-transform: uppercase;
        margin-bottom: 0.55rem;
    }

    .stTextArea textarea {
        background: #11111a !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: 14px !important;
        font-family: 'DM Sans', sans-serif !important;
        line-height: 1.7 !important;
    }

    .stTextArea textarea:focus {
        border-color: var(--purple-bright) !important;
        box-shadow: 0 0 0 1px var(--purple-bright) !important;
    }

    .stButton > button {
        background: linear-gradient(110deg, #8b5cf6, #6d4bd1);
        color: white;
        border: 1px solid #a78bfa;
        border-radius: 10px;
        min-height: 3rem;
        font-weight: 700;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #c4b5fd;
        box-shadow: 0 0 22px #8b5cf633;
        color: white;
        transform: translateY(-1px);
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(19, 19, 28, 0.82);
        border-color: var(--border) !important;
        border-radius: 15px;
    }

    .stCaption, [data-testid="stCaptionContainer"] {
        color: var(--muted);
    }

    hr {
        border-color: var(--border);
    }

    .footer {
        color: #858397;
        font-size: 0.82rem;
        text-align: center;
        padding-top: 2rem;
    }

    @media (max-width: 700px) {
        .block-container {
            padding-top: 1.3rem;
        }
        .hero-title {
            letter-spacing: -1.5px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    '<div class="brand">CINE<span>SAGE</span> <span style="color:#77758a;">/ AI STUDIO</span></div>',
    unsafe_allow_html=True,
)

st.markdown("---")

st.markdown(
    '<div class="eyebrow">MOVIE INTELLIGENCE · POWERED BY AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero-title">Every movie has a story.<br><span>Let AI uncover it.</span></div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-copy">
        Turn a movie description into organized, useful information.
        Extract the cast, director, plot, themes and more from a paragraph
        using structured AI output.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# --------------------------------------------------
# Structured output schema — original fields preserved
# --------------------------------------------------
class MovieInfo(BaseModel):
    title: str
    director: str
    release_year: Optional[str] = None
    genre: str
    cast: List[str]
    story_plot: str
    setting: str
    main_theme: str
    music_composer: str
    imdb_rating: Optional[float] = None
    summary: str


parser = PydanticOutputParser(pydantic_object=MovieInfo)

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Extract important information from the supplied movie paragraph.

            Return the result according to these instructions:
            {format_instructions}

            Rules:
            - Use only information provided in the paragraph.
            - Never invent missing facts or IMDb ratings.
            - Use "Not mentioned" for missing text fields.
            - Use null for a missing release year or IMDb rating.
            - Include all actors explicitly mentioned in the paragraph.
            - Keep the plot concise and the summary to 2-3 sentences.
            """,
        ),
        ("human", "Movie paragraph:\n{paragraph}"),
    ]
)

# --------------------------------------------------
# Input area
# --------------------------------------------------
st.markdown(
    '<div class="section-label">01 / YOUR SOURCE MATERIAL</div>',
    unsafe_allow_html=True,
)
st.subheader("Start with a movie description")
st.caption(
    "Paste a movie synopsis, article excerpt, or description. "
    "CineSage extracts only the details present in your text."
)

with st.container(border=True):
    paragraph = st.text_area(
        "Movie description",
        height=210,
        placeholder=(
            "Example: Inception is a 2010 science-fiction film directed "
            "by Christopher Nolan, starring Leonardo DiCaprio..."
        ),
        label_visibility="collapsed",
        key="movie_paragraph",
    )

    char_count = len(paragraph)
    st.caption(f"{char_count:,} characters")

    extract_clicked = st.button(
        "✦  Extract Movie Intelligence",
        use_container_width=True,
        type="primary",
    )

# --------------------------------------------------
# Run extraction
# --------------------------------------------------
if extract_clicked:
    if not paragraph.strip():
        st.warning("Add a movie description first, then try again.")
    else:
        try:
            with st.spinner("Analyzing your text and structuring the results..."):
                model = ChatGroq(
                    model="openai/gpt-oss-20b",
                    temperature=0,
                )

                prompt = prompt_template.invoke(
                    {
                        "paragraph": paragraph.strip(),
                        "format_instructions": parser.get_format_instructions(),
                    }
                )

                response = model.invoke(prompt)
                movie_info = parser.parse(response.content)

            st.session_state["cinesage_result"] = movie_info
            st.success("Movie intelligence extracted successfully.")

        except Exception as exc:
            st.error(
                "CineSage couldn't complete the extraction. "
                "Check your Groq API key, model availability, and connection, "
                "then try again."
            )
            with st.expander("Technical details"):
                st.code(str(exc))

# --------------------------------------------------
# Results
# --------------------------------------------------
movie_info = st.session_state.get("cinesage_result")

if movie_info:
    st.write("")
    st.markdown("---")
    st.markdown(
        '<div class="section-label">02 / EXTRACTION RESULTS</div>',
        unsafe_allow_html=True,
    )

    st.title(movie_info.title)

    meta_left, meta_middle, meta_right = st.columns(3)

    with meta_left:
        with st.container(border=True):
            st.caption("DIRECTOR")
            st.markdown(f"**{movie_info.director}**")

    with meta_middle:
        with st.container(border=True):
            st.caption("RELEASE YEAR")
            st.markdown(f"**{movie_info.release_year or 'Not mentioned'}**")

    with meta_right:
        with st.container(border=True):
            st.caption("GENRE")
            st.markdown(f"**{movie_info.genre}**")

    st.write("")

    left, right = st.columns([1.15, 0.85], gap="large")

    with left:
        with st.container(border=True):
            st.markdown("### ✦ Story & Plot")
            st.write(movie_info.story_plot)

        with st.container(border=True):
            st.markdown("### ◈ Main Theme")
            st.write(movie_info.main_theme)

        with st.container(border=True):
            st.markdown("### ✎ Summary")
            st.write(movie_info.summary)

    with right:
        with st.container(border=True):
            st.markdown("### ♟ Cast")
            if movie_info.cast:
                for actor in movie_info.cast:
                    st.markdown(f"- {actor}")
            else:
                st.write("Not mentioned")

        with st.container(border=True):
            st.markdown("### ◎ Setting")
            st.write(movie_info.setting)

        with st.container(border=True):
            st.markdown("### ♫ Music / Composer")
            st.write(movie_info.music_composer)

        with st.container(border=True):
            st.markdown("### ★ IMDb Rating")
            if movie_info.imdb_rating is not None:
                st.metric("Rating", f"{movie_info.imdb_rating:.1f} / 10")
            else:
                st.write("Not mentioned")

    st.write("")
    st.download_button(
        "↓  Download structured results (JSON)",
        data=movie_info.model_dump_json(indent=2),
        file_name="cinesage_movie_info.json",
        mime="application/json",
        use_container_width=True,
    )

st.markdown("---")
st.markdown(
    '<div class="footer">CineSage · An AI-powered movie intelligence project</div>',
    unsafe_allow_html=True,
)
