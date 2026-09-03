# 🤖 AI PDF Chatbot — RAG Pipeline

An AI-powered PDF Chatbot built using **Python, LangChain, ChromaDB, Hugging Face Embeddings, Groq LLM, and FastAPI**.

This project uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from a PDF document and generate accurate, context-based answers using an LLM.

---

## 📌 Overview

The AI PDF Chatbot allows users to ask questions about the content of a PDF document.

Instead of directly asking the LLM to answer a question, the application first:

1. Loads the PDF
2. Extracts the text
3. Splits the text into smaller chunks
4. Generates embeddings for each chunk
5. Stores the embeddings in ChromaDB
6. Retrieves the most relevant chunks for a user's question
7. Sends the retrieved context to the Groq LLM
8. Generates the final answer

This approach helps the LLM provide answers based on the actual content of the uploaded document.

---

# 🚀 Features

- 📄 PDF document processing
- ✂️ Intelligent text chunking
- 🧠 Hugging Face sentence embeddings
- 🗄️ ChromaDB vector database
- 🔎 Semantic similarity search
- 🤖 Groq LLM integration
- 📚 Context-based question answering
- ⚡ FastAPI REST API
- 📖 Interactive Swagger API documentation
- 🛡️ Reduced hallucination through document-based context

---

# 🏗️ RAG Architecture

```text
                         PDF Document
                              │
                              ▼
                       PDF Text Extraction
                              │
                              ▼
                         Text Chunking
                              │
                              ▼
                          Embeddings
                              │
                              ▼
                           ChromaDB
                              │
                              │
                         Vector Search
                              │
                              ▼
                       User Question
                              │
                              ▼
                      Query Embedding
                              │
                              ▼
                      Similarity Search
                              │
                              ▼
                    Relevant Document Chunks
                              │
                              ▼
                     Context + Question
                              │
                              ▼
                          Groq LLM
                              │
                              ▼
                        Final Answer
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Application and RAG pipeline |
| 🔗 LangChain | RAG framework |
| ⚡ FastAPI | Backend REST API |
| 🗄️ ChromaDB | Vector database |
| 🤗 Hugging Face | Embedding model |
| 🧠 Sentence Transformers | Text embeddings |
| 🚀 Groq | Large Language Model |
| 📄 PyPDF | PDF text extraction |

---

# 📂 Project Structure

```text
rag-pdf-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── rag.py
│   └── ingest.py
│
├── chroma.db/
│
├── document/
│   └── sample.pdf
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 📌 Project Files

### `app/ingest.py`

Responsible for processing the PDF and creating the vector database.

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embedding Generation
 ↓
ChromaDB
```

---

### `app/rag.py`

Responsible for retrieving relevant chunks and generating answers.

```text
User Question
 ↓
Retriever
 ↓
Relevant Chunks
 ↓
Context Creation
 ↓
Groq LLM
 ↓
Final Answer
```

---

### `app/main.py`

Provides the FastAPI backend and exposes the `/ask` endpoint.

---

### `chroma.db/`

Stores the generated vector embeddings and document data used for semantic retrieval.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd rag-pdf-chatbot
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

The `.env` file contains your private API key.

> ⚠️ Never upload your API key to GitHub.

---

# 📄 Add a PDF Document

Place your PDF inside the `document` folder.

Example:

```text
document/
└── sample.pdf
```

You can replace `sample.pdf` with your own PDF.

---

# 🧠 Create the Vector Database

Run the ingestion script:

```bash
python app/ingest.py
```

The script performs the following operations:

```text
PDF
 ↓
Extract Text
 ↓
Split Text into Chunks
 ↓
Generate Embeddings
 ↓
Store Embeddings
 ↓
ChromaDB
```

After successful execution, the vector database will be created.

---

# ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

You should see:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

From there you can test the RAG API directly from your browser.

---

# 🔎 Ask Questions from the PDF

Use the following endpoint:

```text
POST /ask
```

### Request

```json
{
  "question": "What is this document about?"
}
```

### Response

```json
{
  "question": "What is this document about?",
  "answer": "The document is about..."
}
```

---

# 🔄 How the RAG Pipeline Works

## 1️⃣ PDF Loading

The PDF is loaded using `PyPDFLoader`.

```text
PDF
 ↓
Document Objects
```

Each page of the PDF is converted into a document object that can be processed by LangChain.

---

## 2️⃣ Text Chunking

Large documents are split into smaller pieces.

The project uses:

```text
RecursiveCharacterTextSplitter
```

Example:

```text
Large Document
      │
      ├── Chunk 1
      ├── Chunk 2
      ├── Chunk 3
      ├── Chunk 4
      └── ...
```

Chunking makes it easier to retrieve only the relevant parts of a document.

---

## 3️⃣ Generate Embeddings

Each text chunk is converted into a numerical vector.

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Example:

```text
Text Chunk
     │
     ▼
Embedding Model
     │
     ▼
[0.23, -0.51, 0.72, ...]
```

The embedding represents the semantic meaning of the text.

---

## 4️⃣ Store in ChromaDB

The generated embeddings are stored in ChromaDB.

```text
Text
 ↓
Embedding
 ↓
ChromaDB
```

ChromaDB allows the application to perform similarity searches efficiently.

---

## 5️⃣ User Asks a Question

For example:

```text
"What is the main purpose of this document?"
```

The question is also converted into an embedding.

```text
User Question
      ↓
Query Embedding
```

---

## 6️⃣ Retrieve Relevant Chunks

The query embedding is compared with the vectors stored in ChromaDB.

```text
Query
  ↓
Similarity Search
  ↓
Most Relevant Chunks
```

The retriever returns the most relevant pieces of information from the document.

---

## 7️⃣ Create Context

The retrieved chunks are combined into a context.

```text
Chunk 1
Chunk 2
Chunk 3
   │
   ▼
Context
```

---

## 8️⃣ Send Context to Groq

The context and user's question are passed to the Groq LLM.

```text
Context + Question
        │
        ▼
     Groq LLM
        │
        ▼
   Final Answer
```

The model is instructed to answer based on the retrieved document context.

---

# 🎯 Why Use RAG?

A normal LLM may not have access to information contained inside a user's private PDF.

RAG solves this problem by retrieving relevant information from the document before generating the answer.

### Advantages

- 📚 Works with private documents
- 🔎 Retrieves relevant information
- 🎯 Provides document-specific answers
- 🧠 Gives additional context to the LLM
- 🛡️ Helps reduce hallucinations
- 🔄 Can be extended to multiple documents

---

# 🧪 Example Workflow

### User Question

```text
What is the main topic of this document?
```

### RAG Process

```text
User Question
      ↓
Query Embedding
      ↓
ChromaDB Search
      ↓
Relevant Chunks
      ↓
Context
      ↓
Groq LLM
      ↓
Final Answer
```

### Example Answer

```text
The document mainly discusses the concepts and information
presented in the provided PDF.
```

---

# 📸 Screenshots

## 1. GitHub Repository Structure

This screenshot shows the project files and repository structure.

![Project Structure](Screenshot%202026-09-03%20161812.png)

---

## 2. Application Interface

Project execution and application setup.

![Application](Screenshot%202026-09-03%20161824.png)

---

## 3. RAG Processing

Screenshot showing the RAG pipeline / processing output.

![RAG Processing](Screenshot%202026-09-03%20161905.png)

---

## 4. API Testing

FastAPI / Swagger API testing and response.

![API Testing](Screenshot%202026-09-03%20161948.png)

---

# 🔐 Security

The following files should not be committed to GitHub:

```text
.env
venv/
__pycache__/
```

Recommended `.gitignore`:

```gitignore
venv/
.env
__pycache__/
*.pyc
```

If you don't want to store the generated vector database in GitHub, you can also add:

```gitignore
chroma.db/
```

---

# 📈 Future Improvements

The current project can be extended with several features:

- [ ] React frontend
- [ ] PDF upload through UI
- [ ] Multiple PDF support
- [ ] Chat history
- [ ] Source document references
- [ ] Page number references
- [ ] Streaming LLM responses
- [ ] User authentication
- [ ] Conversation memory
- [ ] Cloud deployment
- [ ] Support for DOCX and TXT files
- [ ] Better chunking strategies

---

# 🌐 Future Architecture

The project can later be extended into a complete full-stack application.

```text
                       React Frontend
                              │
                              ▼
                          FastAPI
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
               PDF Upload          User Question
                    │                   │
                    ▼                   ▼
             Document Processing    Retriever
                    │                   │
                    ▼                   ▼
                 ChromaDB          Relevant Chunks
                                        │
                                        ▼
                                   Groq LLM
                                        │
                                        ▼
                                   AI Answer
                                        │
                                        ▼
                                  React UI
```

---

# 💡 Key Concepts Learned

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation
- Vector databases
- Semantic search
- Text embeddings
- Document chunking
- LangChain
- LLM integration
- FastAPI REST APIs
- Prompt engineering
- PDF processing

---

# 👨‍💻 Author

## Harsh Gupta

A practical implementation of a **Retrieval-Augmented Generation (RAG) PDF Chatbot** using Python and modern AI technologies.

### Technologies Used

```text
Python
LangChain
FastAPI
ChromaDB
Hugging Face
Sentence Transformers
Groq
PyPDF
```

---

## ⭐ If you found this project useful, consider giving it a star!
