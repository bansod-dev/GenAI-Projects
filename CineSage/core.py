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


# Paragraph to analyze
paragraph =input("Enter a paragraph about a movie: ")

# Fill the template with our paragraph
prompt = prompt_template.invoke({
    "paragraph": paragraph
})


# Send prompt to the model
response = model.invoke(prompt)


# Print result
print(response.content)