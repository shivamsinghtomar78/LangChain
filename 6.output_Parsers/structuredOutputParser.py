from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


# Load environment variables
load_dotenv()   

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

schema=[
    ResponseSchema(name="fact_1",description="A fact 1 about topic"),
    ResponseSchema(name="fact_2",description="A fact 2 about topic"),
    ResponseSchema(name="fact_3",description="A fact 3 about topic")
    
] 

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give me 3 facts about the topic {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
chain=template | model | parser

result = chain.invoke({"topic":"Python programming language"})
print(result)



# prompt=template.invoke({"topic":"Python programming language"})
# result=model.invoke(prompt)
# final=parser.parse(result.content)
# print(final)