from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma




loader = PyPDFLoader("document/sample.pdf")
documents = loader.load()

print('Number of pages in the PDF:', len(documents))

for document in documents[:2]:
    print(document.page_content[:500])
    print("----------------")

text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_spliter.split_documents(documents)

print("chunks len", len(chunks))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("embeddings model load")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=os.path.join(BASE_DIR, "chroma.db")
)

print("Vectorstore created successfully!")
