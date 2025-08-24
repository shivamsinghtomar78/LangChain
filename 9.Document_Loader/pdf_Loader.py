from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader  # updated import

# Load the PDF
loader = PyPDFLoader("dl-curriculum.pdf")
docs = loader.load()

# Print number of pages/documents loaded
print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)