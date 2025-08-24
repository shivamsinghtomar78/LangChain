from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader=DirectoryLoader(
    path="Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load()

for document in docs:
    print(document.page_content[:1000])
    print(document.metadata)

