from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from  langchain_core.output_parsers import StrOutputParser
load_dotenv()
model= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)
prompt=PromptTemplate(
     template="Generate 5 interesting fact about {topic}",
     input_variables=["topic"]
 )


parser=StrOutputParser()

chain= prompt | model | parser


result=chain.invoke({"topic":"Python programming language"})
print(result)


chain.get_graph().print_ascii()