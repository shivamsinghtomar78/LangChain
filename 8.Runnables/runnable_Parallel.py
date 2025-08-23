from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()
prompt1=PromptTemplate(
    template ="Generate a tweet about {topic}.",
    input_variables=["topic"],
)
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)
parser=StrOutputParser()

prompt2=PromptTemplate(
    template="Generate a Linkedin post about  -{topic}",
    input_variables=["topic"]
)

parallel_chain=RunnableParallel(
    {
        "tweet":RunnableSequence(prompt1, model, parser),
        "linkedin":RunnableSequence(prompt2, model, parser)
    }
)

result=parallel_chain.invoke({"topic":"sarcastic comment on delhi stray dogs topic"})

print(result)