from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()
model= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)
chat_history = [
    SystemMessage(content="You are a helpful assistant that translates English to spanish."), 
]

while True:
    user_input =input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"Chatbot: {result.content}")