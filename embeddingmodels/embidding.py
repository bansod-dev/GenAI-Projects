from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Generative AI can create new content."

vector = embeddings.embed_query(text)

print(vector)
print(len(vector))