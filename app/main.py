from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import ask_question

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Rag is running"}

@app.post("/ask")
def ask(data: Question):
    answer = ask_question(data.question)
    return {
        "question": data.question,
        "answer": answer
    }
