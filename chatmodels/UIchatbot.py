from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

message_history = [
    SystemMessage(content="You are my ai assistant teacher.")
]

print("-------------new conversation (print 'stop' to end)----------------")

while True:
    
    prompt = input("you: ")
    
    if prompt.lower() == "stop":
        break

    message_history.append(HumanMessage(content=prompt))

    response = model.invoke(message_history)

    message_history.append(AIMessage(content=response.content))

    print("bot:", response.content)

print(message_history)    