from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()   

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

# 1st prompt --> detailed report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt --> summary
template2 = PromptTemplate(
    template="write a 5 line summary on the following text: {text}",
    input_variables=["text"]
)


prompt1=template1.invoke({"topic":"Artificial Intelligence"})
result= model.invoke(prompt1)

prompt2=template2.invoke({"text":result.content})

result1=model.invoke(prompt2)

print(result1.content)