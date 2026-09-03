# 🤖 AI PDF Chatbot — RAG Pipeline

An AI-powered PDF chatbot built using **Python, LangChain, ChromaDB, Hugging Face Embeddings, Groq LLM, and FastAPI**.

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows users to ask questions about the content of a PDF document and receive answers based on the relevant information retrieved from the document.

---

## 🚀 Features

- 📄 PDF document processing
- ✂️ Text chunking
- 🧠 Hugging Face embeddings
- 🗄️ ChromaDB vector database
- 🔎 Semantic similarity search
- 🤖 Groq LLM integration
- 📚 Context-based question answering
- ⚡ FastAPI backend
- 📖 Automatic Swagger API documentation
- 🛡️ Reduces hallucination by providing relevant document context

---

## 🏗️ RAG Architecture

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
                 ───── Retrieval ─────
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

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend & RAG pipeline |
| LangChain | RAG framework |
| FastAPI | REST API |
| ChromaDB | Vector database |
| Hugging Face | Embeddings |
| Sentence Transformers | Embedding model |
| Groq | Large Language Model |
| PyPDF | PDF text extraction |

---

## 📂 Project Structure

```text
rag-pdf-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── rag.py
│   └── ingest.py
│
├── documents/
│   └── sample.pdf
│
├── screenshots/
│   ├── project-structure.png
│   ├── swagger-api.png
│   └── rag-response.png
│
├── chroma_db/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📌 File Responsibilities

### `ingest.py`

Handles the document ingestion pipeline.

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embeddings
 ↓
ChromaDB
```

### `rag.py`

Handles the question-answering pipeline.

```text
Question
 ↓
Retriever
 ↓
Relevant Chunks
 ↓
Context
 ↓
Groq LLM
 ↓
Answer
```

### `main.py`

Provides the FastAPI REST API and exposes the `/ask` endpoint.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

> ⚠️ Never commit your `.env` file or API key to GitHub.

---

## 📄 Add a PDF

Place your PDF inside the `documents` folder.

Example:

```text
documents/
└── sample.pdf
```

---

## 🧠 Create the Vector Database

Run the ingestion script:

```bash
python app/ingest.py
```

This performs:

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding Generation
 ↓
ChromaDB
```

After successful execution, the `chroma_db` directory will contain the vector database.

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

You will see the available API endpoints.

---

## 🔎 Ask a Question

Use the:

```text
POST /ask
```

endpoint.

Example request:

```json
{
  "question": "What is this document about?"
}
```

Example response:

```json
{
  "question": "What is this document about?",
  "answer": "The document is about..."
}
```

---

# 📸 Screenshots

## 1. Project Structure

The GitHub repository structure of the RAG PDF Chatbot.

![Project Structure](screenshots/project-structure.png)

---

## 2. Swagger API

FastAPI Swagger UI used to test the RAG API.

![Swagger API](screenshots/swagger-api.png)

---

## 3. RAG Response

The system retrieves relevant information from the PDF and generates an answer using the Groq LLM.

![RAG Response](screenshots/rag-response.png)

---

# 🔄 How the RAG Pipeline Works

## 1. Document Loading

The PDF is loaded using `PyPDFLoader`.

```text
PDF → Documents
```

Each page is converted into a LangChain `Document` object.

---

## 2. Text Chunking

Large documents are divided into smaller chunks using:

```text
RecursiveCharacterTextSplitter
```

Example:

```text
Document
   │
   ├── Chunk 1
   ├── Chunk 2
   ├── Chunk 3
   └── Chunk 4
```

The project uses:

```text
chunk_size = 500
chunk_overlap = 50
```

---

## 3. Embeddings

Each text chunk is converted into a numerical vector using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Example:

```text
Text Chunk
    ↓
Embedding Model
    ↓
[0.21, -0.45, 0.78, ...]
```

These vectors represent the semantic meaning of the text.

---

## 4. Vector Storage

The embeddings are stored in **ChromaDB**.

```text
Text Chunk
    ↓
Embedding
    ↓
ChromaDB
```

This allows efficient similarity-based retrieval.

---

## 5. Retrieval

When a user asks a question, the question is also converted into an embedding.

```text
User Question
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
```

The retriever returns the most relevant document chunks.

---

## 6. Context Creation

The retrieved chunks are combined to create the context.

```text
Relevant Chunk 1
Relevant Chunk 2
Relevant Chunk 3
        ↓
     Context
```

---

## 7. Generation

The context and user's question are sent to the Groq LLM.

```text
Context + Question
        ↓
      Groq LLM
        ↓
   Final Answer
```

The model is instructed to answer using the provided document context.

---

# 🎯 Why RAG?

A normal LLM may not have access to information contained inside a private PDF.

RAG solves this problem by retrieving relevant information from the document before generating the answer.

### Benefits

- 📚 Works with private documents
- 🔎 Retrieves relevant information
- 🧠 Provides additional context to the LLM
- 🎯 Improves answer relevance
- 🛡️ Helps reduce hallucinations

---

# 🧪 Example

### User Question

```text
What is the main purpose of this document?
```

### RAG Pipeline

```text
Question
   ↓
Embedding
   ↓
ChromaDB Search
   ↓
Top Relevant Chunks
   ↓
Context
   ↓
Groq LLM
   ↓
Answer
```

### Generated Answer

```text
The main purpose of the document is to provide
information about the topic discussed in the PDF.
```

---

# 🔐 Security

The following files should not be committed to GitHub:

```text
.env
venv/
chroma_db/
__pycache__/
```

Recommended `.gitignore`:

```gitignore
venv/
.env
__pycache__/
*.pyc
chroma_db/
```

---

# 🔮 Future Improvements

- [ ] React frontend
- [ ] PDF upload through UI
- [ ] Multiple PDF support
- [ ] Chat history
- [ ] Source/page references
- [ ] Streaming responses
- [ ] Authentication
- [ ] Cloud deployment
- [ ] Multiple document formats
- [ ] Improved chunking strategies
- [ ] Conversation memory

---

# 📈 Future Architecture

```text
                    React Frontend
                          │
                          ▼
                      FastAPI
                          │
                          ▼
                    PDF Upload
                          │
                          ▼
                  Document Processing
                          │
                          ▼
                     ChromaDB
                          │
                          ▼
                      Retriever
                          │
                          ▼
                     Groq LLM
                          │
                          ▼
                   AI Generated Answer
```

---

# 👨‍💻 Author

## Harsh Gupta

Built as a practical implementation of a **Retrieval-Augmented Generation (RAG) pipeline using Python, LangChain, ChromaDB, FastAPI, Hugging Face Embeddings, and Groq.**

---

⭐ If you found this project useful, consider giving it a star!
