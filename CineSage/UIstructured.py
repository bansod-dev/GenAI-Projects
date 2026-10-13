import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser


# Load environment variables
load_dotenv()


# Page configuration
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬"
)


# Initialize Groq model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


class MovieInfo(BaseModel):
    title: str
    director: str
    release_year: Optional[str]
    genre: str
    cast: List[str]
    story_plot: str
    setting: str
    main_theme: str
    music_composer: str
    imdb_rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=MovieInfo)


# Create chat prompt template
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Extract the important and useful information from the following paragraph about a movie.

        Return the information in the following format:

        {format_instructions}
        """
    ),
    (
        "human",
        "Paragraph: {paragraph}"
    )
])


# UI
st.title("🎬 Movie Information Extractor")

st.write("Enter a paragraph about a movie and extract structured information from it.")

paragraph = st.text_area(
    "Enter a paragraph about a movie:",
    height=250
)


if st.button("Extract Information"):

    if not paragraph:
        st.warning("Please enter a paragraph about a movie.")

    else:

        # Fill the template with our paragraph
        prompt = prompt_template.invoke({
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        })


        # Send prompt to the model
        response = model.invoke(prompt)

        movie_info = parser.parse(response.content)


        # Display result
        st.subheader("Extracted Information")
        st.write(movie_info)