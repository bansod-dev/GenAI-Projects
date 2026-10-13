import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


# Load environment variables
load_dotenv()


# Initialize Groq model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# Create prompt template
prompt_template = PromptTemplate.from_template("""
You are an information extraction assistant.

Extract the important and useful information from the following paragraph.

Return the information in the following format:

Movie Name:
Director:
Release Year:
Genre:
Cast:
Story / Plot:
Setting:
Main Theme:
Music / Composer:
IMDb Rating:
Reception:
Summary:

Rules:
- Extract information only from the given paragraph.
- Do not invent or assume information that is not present.
- If a field is not mentioned, write "Not mentioned".
- Keep the extracted information concise and clear.
- For Cast, list all mentioned actors.
- The Summary should be 2-3 sentences and capture the main idea of the paragraph.

Paragraph:
{paragraph}
""")


# Streamlit UI
st.title("🎬 Movie Information Extractor")

paragraph = st.text_area(
    "Enter a paragraph about a movie:",
    height=250
)


if st.button("Extract Information"):

    if paragraph:

        # Fill the template with our paragraph
        prompt = prompt_template.invoke({
            "paragraph": paragraph
        })


        # Send prompt to the model
        response = model.invoke(prompt)


        # Display result
        st.subheader("Extracted Information")

        st.write(response.content)

    else:
        st.warning("Please enter a paragraph.")