from langchain_core.prompts import PromptTemplate, load_prompt,ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv

chat_template = ChatPromptTemplate.from_messages(
    [
    ("system", "You are a helpful assistant that translates {domain} to {topic}."),
    ("human", "Translate the following text: {text}")
        
    ]
)

prompt=chat_template.invoke(
    {
        "domain": "Mathematics",    
        "topic": "Integration"
    }
)
print(prompt)