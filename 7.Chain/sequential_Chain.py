from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from  langchain_core.output_parsers import StrOutputParser
load_dotenv()
model= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)

prompt1=PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Generate a 5 pointer from the following text \n {text}",
    input_variables=["text"]
)


parser=StrOutputParser()

chain= prompt1 | model | parser|prompt2 | model | parser

result=chain.invoke({"topic":"Artificial Intelligence"})
print(result)


chain.get_graph().print_ascii()