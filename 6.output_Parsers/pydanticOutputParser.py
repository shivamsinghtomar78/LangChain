from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

# Load environment variables
load_dotenv()   

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

class Person(BaseModel):
    name: str = Field(..., description="Name of the person")
    age: int = Field(..., description="Age of the person")
    city: str = Field(..., description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person.\n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
#without using chain
# prompt = template.format(place="Indian")
# print(prompt)
# result = model.invoke(prompt)
# final = parser.parse(result.content)

# print(final)


# Using chain
chain = template | model | parser
result = chain.invoke({"place": "Indian"})
print(result)
print(result.name)
print(result.age)
print(result.city)
    
