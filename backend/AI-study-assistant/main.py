from fastapi import FastAPI
from agent import ask_agent
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Cloud-Native AI Study Assistant",
    description="AI-powered study assistant with RAG + Tools + Agent",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Models ----------
class Question(BaseModel):
    question: str

# ---------- Routes ----------

@app.get("/")
def root():
    return {
        "message": "Cloud-Native AI Study Assistant API is running 🚀",
        "docs": "/docs",
        "ask_endpoint": "/ask",
        "method": "POST"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(data: Question):
    response = ask_agent(data.question)
    return {"response": response}

