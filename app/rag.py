from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = Chroma(
    persist_directory="./chroma.db",
    embedding_function=embeddings
)

retrival = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

promt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I don't know based on the provided document."
""")

def ask_question(question):
    docs = retrival.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    finalpromt = promt.invoke({
        "context": context,
        "question": question
    })

    response = llm.invoke(finalpromt)
    return response.content
