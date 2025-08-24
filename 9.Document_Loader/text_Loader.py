from langchain.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)
prompt=PromptTemplate(
    template="write a summary for the following poem:\n{poem}",
    input_variables=["poem"]
)

parser=StrOutputParser()

loader=TextLoader("cricket.txt",encoding="utf8")


docs=loader.load()

print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)


chain=prompt | model | parser
response=chain.invoke({"poem":docs[0].page_content})
print(response)