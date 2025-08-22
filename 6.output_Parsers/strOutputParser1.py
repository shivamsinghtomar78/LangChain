from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser= StrOutputParser()
chain=template1 | model | template2 | model | parser

result = chain.invoke({"topic": "Artificial Intelligence"})
print(result)