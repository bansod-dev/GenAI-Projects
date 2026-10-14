
import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Ghanshyam Bansod | AI & Data Science Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# LINKS
# =========================================================
GITHUB_PROFILE = "https://github.com/bansod-dev"
LINKEDIN_PROFILE = "https://www.linkedin.com/in/ghanshyam-bansod-994375320/"

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --bg: #080a12;
        --card: #101321;
        --border: rgba(151, 143, 255, 0.20);
        --purple: #a78bfa;
        --blue: #60a5fa;
        --teal: #5eead4;
        --text: #f3f4f6;
        --muted: #a1a1b5;
    }

    html {
        scroll-behavior: smooth;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 12% 5%, rgba(103, 80, 220, 0.16), transparent 35%),
            radial-gradient(ellipse at 90% 25%, rgba(39, 141, 190, 0.10), transparent 32%),
            var(--bg);
        color: var(--text);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(8, 10, 18, 0.85);
    }

    [data-testid="stSidebar"] {
        background: var(--bg);
    }

    .block-container {
        max-width: 1120px;
        padding-top: 1.6rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3, h4 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: var(--text);
    }

    p, li {
        color: var(--muted);
        line-height: 1.75;
    }

    a {
        color: var(--purple) !important;
        text-decoration: none !important;
    }

    a:hover {
        color: var(--teal) !important;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        padding: 12px 0 24px 0;
        border-bottom: 1px solid var(--border);
        margin-bottom: 42px;
    }

    .brand {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 1.5rem;
        color: white;
    }

    .brand span {
        color: var(--purple);
    }

    .nav-links {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: flex-end;
        font-size: 0.9rem;
    }

    .nav-links a {
        color: #c5c5d6 !important;
    }

    .hero {
        padding: 58px 0 65px 0;
    }

    .eyebrow {
        display: inline-block;
        color: var(--teal);
        border: 1px solid rgba(94, 234, 212, 0.30);
        background: rgba(94, 234, 212, 0.06);
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 0.82rem;
        letter-spacing: 0.4px;
        margin-bottom: 22px;
    }

    .hero h1 {
        font-size: clamp(2.8rem, 7vw, 5.3rem);
        line-height: 1.05;
        letter-spacing: -3px;
        margin: 0 0 22px 0;
        font-weight: 700;
    }

    .gradient-text {
        background: linear-gradient(95deg, #c4b5fd, #60a5fa, #5eead4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        max-width: 690px;
        font-size: 1.08rem;
        color: #b4b5c8;
        line-height: 1.9;
        margin-bottom: 27px;
    }

    .hero-links {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 25px;
    }

    .hero-link {
        display: inline-block;
        padding: 11px 17px;
        border: 1px solid var(--border);
        border-radius: 9px;
        background: rgba(255, 255, 255, 0.025);
        color: #e7e5ff !important;
        font-weight: 600;
        transition: 0.2s ease;
    }

    .hero-link:hover {
        border-color: var(--purple);
        background: rgba(167, 139, 250, 0.10);
    }

    .section-heading {
        font-size: 2rem;
        margin-top: 0;
        margin-bottom: 8px;
        letter-spacing: -0.8px;
    }

    .section-description {
        color: var(--muted);
        margin-bottom: 28px;
    }

    .section {
        padding-top: 35px;
        padding-bottom: 35px;
    }

    .info-card {
        background: linear-gradient(
            145deg,
            rgba(20, 23, 41, 0.95),
            rgba(12, 15, 27, 0.95)
        );
        border: 1px solid var(--border);
        border-radius: 15px;
        padding: 23px;
        min-height: 165px;
        margin-bottom: 12px;
        transition: 0.2s ease;
    }

    .info-card:hover {
        border-color: rgba(167, 139, 250, 0.65);
        transform: translateY(-2px);
    }

    .info-card h3 {
        font-size: 1.1rem;
        margin: 0 0 10px 0;
    }

    .info-card p {
        font-size: 0.93rem;
        margin-bottom: 0;
    }

    .project-card {
        background: linear-gradient(
            145deg,
            rgba(20, 23, 41, 0.98),
            rgba(12, 15, 27, 0.98)
        );
        border: 1px solid var(--border);
        border-radius: 15px;
        padding: 23px;
        min-height: 285px;
        margin-bottom: 9px;
        transition: 0.22s ease;
    }

    .project-card:hover {
        border-color: rgba(167, 139, 250, 0.70);
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.18);
    }

    .project-type {
        color: var(--teal);
        font-size: 0.76rem;
        text-transform: uppercase;
        letter-spacing: 1.3px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .project-card h3 {
        font-size: 1.3rem;
        margin: 0 0 12px 0;
    }

    .project-card p {
        font-size: 0.91rem;
        line-height: 1.75;
        min-height: 76px;
        margin-bottom: 17px;
    }

    .tag {
        display: inline-block;
        border: 1px solid rgba(167, 139, 250, 0.19);
        background: rgba(167, 139, 250, 0.07);
        color: #c8c2ff;
        padding: 4px 9px;
        border-radius: 6px;
        font-size: 0.74rem;
        margin: 0 5px 6px 0;
    }

    .project-links {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 16px;
        font-size: 0.88rem;
        font-weight: 600;
    }

    .project-links a {
        display: inline-block;
        padding: 8px 10px;
        border: 1px solid var(--border);
        border-radius: 7px;
        background: rgba(255, 255, 255, 0.025);
    }

    .project-links a:hover {
        border-color: var(--purple);
    }

    .skill-group {
        background: rgba(16, 19, 33, 0.90);
        border: 1px solid var(--border);
        border-radius: 13px;
        padding: 20px;
        margin-bottom: 13px;
    }

    .skill-group h3 {
        color: var(--purple);
        font-size: 1.05rem;
        margin: 0 0 13px 0;
    }

    .skill-pill {
        display: inline-block;
        color: #d5d6e7;
        border: 1px solid rgba(255, 255, 255, 0.10);
        background: rgba(255, 255, 255, 0.035);
        padding: 7px 11px;
        border-radius: 7px;
        font-size: 0.83rem;
        margin: 0 6px 7px 0;
    }

    .contact-card {
        text-align: center;
        padding: 38px 25px;
        background:
            radial-gradient(ellipse at top, rgba(112, 87, 220, 0.15), transparent 70%),
            rgba(16, 19, 33, 0.92);
        border: 1px solid var(--border);
        border-radius: 18px;
    }

    .contact-card h2 {
        font-size: 2rem;
        margin-bottom: 10px;
    }

    .footer {
        text-align: center;
        color: #777b91;
        font-size: 0.82rem;
        padding: 28px 0 5px 0;
        border-top: 1px solid var(--border);
        margin-top: 45px;
    }

    div[data-testid="stMarkdownContainer"] {
        overflow-wrap: anywhere;
    }

    @media (max-width: 700px) {
        .navbar {
            align-items: flex-start;
            flex-direction: column;
        }

        .nav-links {
            justify-content: flex-start;
            gap: 13px;
        }

        .hero {
            padding-top: 28px;
        }

        .hero h1 {
            letter-spacing: -1.5px;
        }

        .project-card {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# NAVIGATION
# =========================================================
st.markdown(
    f"""
    <div class="navbar">
        <div class="brand">GB<span>.</span></div>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#skills">Skills</a>
            <a href="#contact">Contact</a>
            <a href="{GITHUB_PROFILE}" target="_blank">GitHub ↗</a>
            <a href="{LINKEDIN_PROFILE}" target="_blank">LinkedIn ↗</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HERO
# =========================================================
st.markdown(
    f"""
    <div class="hero">
        <div class="eyebrow">✦ AI &amp; Data Science Portfolio</div>
        <h1>
            Building things<br>
            <span class="gradient-text">with intelligence.</span>
        </h1>
        <p class="hero-description">
            I'm Ghanshyam Bansod, an AI &amp; Data Science student interested
            in machine learning, deep learning, and generative AI.
            I enjoy turning ideas into practical projects, from predictive
            models to AI-powered applications.
        </p>
        <div class="hero-links">
            <a class="hero-link" href="#projects">Explore My Projects ↓</a>
            <a class="hero-link" href="{GITHUB_PROFILE}" target="_blank">GitHub ↗</a>
            <a class="hero-link" href="{LINKEDIN_PROFILE}" target="_blank">LinkedIn ↗</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# ABOUT
# =========================================================
st.markdown(
    """
    <div class="section" id="about">
        <h2 class="section-heading">About Me<span class="gradient-text">.</span></h2>
        <p class="section-description">
            Learning by building, experimenting, and solving real problems.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

about_columns = st.columns(3, gap="large")

about_cards = [
    (
        "01 / Data Science",
        "From data to decisions",
        "Exploring data analysis, statistics, feature engineering, and "
        "machine learning to uncover patterns and build predictive models.",
    ),
    (
        "02 / Deep Learning",
        "Neural networks in practice",
        "Working with artificial neural networks, convolutional neural "
        "networks, and practical classification problems.",
    ),
    (
        "03 / Generative AI",
        "Building AI applications",
        "Exploring LLMs, LangChain, embeddings, chat applications, and "
        "retrieval-augmented generation concepts.",
    ),
]

for column, card in zip(about_columns, about_cards):
    with column:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="project-type">{card[0]}</div>
                <h3>{card[1]}</h3>
                <p>{card[2]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# =========================================================
# PROJECT DATA
# =========================================================
projects = [
    {
        "category": "Generative AI",
        "title": "CineSage",
        "description": (
            "A movie-focused AI project exploring conversational interfaces "
            "and structured LLM responses."
        ),
        "tags": ["GenAI", "LLMs", "LangChain", "Streamlit"],
        "url": "https://github.com/bansod-dev/GenAI-Projects/tree/main/CineSage",
        "demo": "https://genai-projects-3hmgd8gx28e4nhzuhnp6xp.streamlit.app/",
    },
    {
        "category": "Machine Learning",
        "title": "Insurance Charges Prediction",
        "description": (
            "A regression project that predicts medical insurance charges "
            "using customer features and evaluates model performance."
        ),
        "tags": ["Python", "Pandas", "Scikit-learn", "Regression"],
        "url": "https://github.com/bansod-dev/insurance-charges-prediction",
        "demo": (
            "https://insurance-charges-prediction-pfnlkwf7iuzzpvdmresdwf.streamlit.app/"
        ),
    },
    {
        "category": "Machine Learning",
        "title": "Heart Disease Prediction",
        "description": (
            "A classification application using Logistic Regression and "
            "feature scaling to estimate heart disease risk from input data."
        ),
        "tags": ["Python", "Scikit-learn", "Logistic Regression", "Streamlit"],
        "url": "YOUR_ACTUAL_HEART_DISEASE_REPOSITORY_URL",
        "demo": (
            "https://heartdiseaseprediction-n4wh2dzlobofjaf2ghomuh.streamlit.app/"
        ),
    },
    {
        "category": "Deep Learning",
        "title": "Iris ANN Classifier",
        "description": (
            "An artificial neural network that classifies iris flowers "
            "from their sepal and petal measurements."
        ),
        "tags": ["Python", "TensorFlow", "ANN", "Classification"],
        "url": "https://github.com/bansod-dev/iris-ann-classifier",
        "demo": (
            "https://iris-ann-classifier-fappvhzcuyux8appuwsrfpo8.streamlit.app/"
        ),
    },
    {
        "category": "Deep Learning",
        "title": "MNIST Digit Classifier",
        "description": (
            "An image classification project exploring handwritten digit "
            "recognition with perceptron, ANN, and CNN models."
        ),
        "tags": ["Python", "TensorFlow", "CNN", "Computer Vision"],
        "url": "https://github.com/bansod-dev/mnist-digit-classifier",
        "demo": "https://mnist-digit-classifier-4ko5nobnzot2gtgzy28xzw.streamlit.app/",

    },
    {
        "category": "Data Science / ML",
        "title": "Customer Churn Analysis",
        "description": (
            "An end-to-end churn analysis project with classification models "
            "and explainability experiments to understand customer predictions."
        ),
        "tags": ["Pandas", "Scikit-learn", "Random Forest", "SHAP"],
        "url": "https://github.com/bansod-dev/customer-churn-analysis",
        "demo": (
            "https://customer-churn-analysis-gkpfhdqhbndmzboak5z6xq.streamlit.app/"
        ),
    },
    {
        "category": "Generative AI",
        "title": "Dark AI",
        "description": (
            "A dark-themed AI assistant interface built with Streamlit and "
            "a Groq-powered chat model."
        ),
        "tags": ["Python", "Streamlit", "Groq", "LLMs"],
        "url": "https://github.com/bansod-dev/GenAI-Projects/blob/main/portfolio.py",
        "demo": None,
    },
    {
        "category": "Generative AI",
        "title": "Chat Model Experiments",
        "description": (
            "Experiments with chat-model integrations and the building blocks "
            "used to create conversational AI applications."
        ),
        "tags": ["Python", "LangChain", "Chat Models", "GenAI"],
        "url": "https://github.com/bansod-dev/GenAI-Projects/tree/main/chatmodels",
        "demo": None,
    },
    {
        "category": "Generative AI",
        "title": "Text Embeddings",
        "description": (
            "Exploring text embeddings and their role in semantic similarity, "
            "meaning-based retrieval, and modern LLM applications."
        ),
        "tags": ["Python", "Embeddings", "NLP", "GenAI"],
        "url": "https://github.com/bansod-dev/GenAI-Projects/tree/main/embeddingmodels",
        "demo": None,
    },
]

# =========================================================
# PROJECTS
# =========================================================
st.markdown(
    """
    <div class="section" id="projects">
        <h2 class="section-heading">Featured Projects<span class="gradient-text">.</span></h2>
        <p class="section-description">
            A collection of my machine learning, deep learning, data science,
            and generative AI projects. Try a live application or explore its code.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Live demo links are provided for projects with recorded deployments.")

for start in range(0, len(projects), 2):
    columns = st.columns(2, gap="large")

    for column, project in zip(columns, projects[start:start + 2]):
        with column:
            tags_html = "".join(
                f'<span class="tag">{tag}</span>'
                for tag in project["tags"]
            )

            st.markdown(
                f"""
                <div class="project-card">
                    <div class="project-type">{project["category"]}</div>
                    <h3>{project["title"]}</h3>
                    <p>{project["description"]}</p>
                    <div>{tags_html}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            links = []

            if project.get("demo"):
                links.append(
                    f'<a href="{project["demo"]}" target="_blank">'
                    '🚀 Try Live Demo ↗</a>'
                )

            if project.get("url"):
                links.append(
                    f'<a href="{project["url"]}" target="_blank">'
                    '⌘ Source Code ↗</a>'
                )

            if links:
                st.markdown(
                    f'<div class="project-links">{"".join(links)}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.caption("Links coming soon.")

            st.write("")

# =========================================================
# SKILLS
# =========================================================
st.markdown(
    """
    <div class="section" id="skills">
        <h2 class="section-heading">Skills &amp; Technologies<span class="gradient-text">.</span></h2>
        <p class="section-description">
            Tools and concepts I've worked with across my projects and learning.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

skill_groups = [
    (
        "Programming & Data",
        ["Python", "SQL", "NumPy", "Pandas", "Matplotlib", "Seaborn", "Statistics", "Probability"],
    ),
    (
        "Machine Learning",
        ["Scikit-learn", "Regression", "Classification", "Feature Engineering", "Model Evaluation"],
    ),
    (
        "Deep Learning",
        ["TensorFlow", "Keras", "ANN", "CNN", "Neural Networks"],
    ),
    (
        "Generative AI",
        ["LLMs", "LangChain", "Prompt Engineering", "Text Embeddings", "RAG Concepts"],
    ),
    (
        "Tools & Deployment",
        ["Streamlit", "Jupyter Notebook", "Git", "GitHub", "VS Code"],
    ),
]

for start in range(0, len(skill_groups), 2):
    columns = st.columns(2, gap="large")

    for column, group in zip(columns, skill_groups[start:start + 2]):
        with column:
            pills = "".join(
                f'<span class="skill-pill">{skill}</span>'
                for skill in group[1]
            )

            st.markdown(
                f"""
                <div class="skill-group">
                    <h3>{group[0]}</h3>
                    <div>{pills}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# =========================================================
# CONTACT
# =========================================================
st.markdown(
    """
    <div class="section" id="contact">
        <div class="contact-card">
            <div class="eyebrow">Let's Connect</div>
            <h2>Have an idea? Let's talk.</h2>
            <p>
                I'm interested in AI, data science, and opportunities to learn
                and build meaningful projects.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

contact_columns = st.columns(2)

with contact_columns[0]:
    st.markdown(
        f"""
        <div class="info-card">
            <h3>💻 GitHub</h3>
            <p>Explore my code, repositories, and projects.</p>
            <a href="{GITHUB_PROFILE}" target="_blank">github.com/bansod-dev ↗</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with contact_columns[1]:
    st.markdown(
        f"""
        <div class="info-card">
            <h3>💼 LinkedIn</h3>
            <p>Connect with me professionally.</p>
            <a href="{LINKEDIN_PROFILE}" target="_blank">
                LinkedIn Profile ↗
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        Built with Python &amp; Streamlit · Designed with curiosity ✦
    </div>
    """,
    unsafe_allow_html=True,
)
