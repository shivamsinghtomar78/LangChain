from langchain_core.prompts import PromptTemplate, load_prompt, ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

# chat template
chat_template = ChatPromptTemplate([
    ("system", "you are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []

# load chat history
try:
    with open("chat_history.txt", "r") as f:
        chat_history = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("Chat history file not found. Starting with empty history.")

print(chat_history)

# create chat prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "where is my refund?"
})

print(prompt)