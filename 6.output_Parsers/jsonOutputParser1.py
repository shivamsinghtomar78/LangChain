from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser


# Load environment variables
load_dotenv()   

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)
parser=JsonOutputParser()
# 1st prompt --> detailed report
template= PromptTemplate(
    template="Give me the name ,age and city of a fictional student \n {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
    
)
chain=template | model | parser
result = chain.invoke({})
print(result)
print(result["name"])
print(result["age"])
print(result["city"])