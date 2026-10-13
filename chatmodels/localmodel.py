from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "do_sample": False,
    }
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("What is generative AI?")

print(response.content)