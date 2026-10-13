import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv(r"C:\Users\ghans\Desktop\Gen AI\.env")

hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

print("Token loaded:", hf_token is not None)

lmm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(
    llm=lmm,
    temperature=0.7
)

response = model.invoke("Who are you?")

print(response.content)