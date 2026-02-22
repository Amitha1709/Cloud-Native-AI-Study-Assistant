#  Cloud-Native AI Study Assistant

An end-to-end **cloud-native AI assistant** that answers academic questions, performs calculations, and retrieves knowledge from custom study materials using RAG (Retrieval-Augmented Generation).

Built with a modern serverless mindset and deployed on AWS infrastructure.

---

##  Live Architecture

**Frontend:** React (S3 Static Hosting + CloudFront)
**Backend:** FastAPI on AWS EC2
**AI Layer:** Hugging Face Inference API
**RAG Engine:** LangChain + FAISS
**Cloud:** AWS

---

##  Features

*  AI-powered question answering
*  RAG over custom PDF notes
*  Smart calculator detection
*  Weather/news intent routing
*  FastAPI high-performance backend
*  Modern React chat UI
*  Cloud-native deployment on AWS
*  Environment-based secret management
*  CORS-enabled production API

---

##  How It Works

1. User asks question in React UI

2. Request goes to FastAPI backend

3. Agent routes the query:

   * Math → Calculator tool
   * Weather/News → Search tool
   * Academic → RAG pipeline
   * General → Hugging Face LLM

4. Response returned to frontend

---

##  Architecture Diagram

```
User → React (S3 + CloudFront)
        ↓
     FastAPI (EC2)
        ↓
   AI Agent Router
      ↙    ↓     ↘
 Calculator  RAG   HF LLM
```

---

##  Project Structure

```
Cloud-Native-AI-Study-Assistant/
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── rag.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

##  Local Setup

### 1️⃣ Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 2️⃣ Frontend

```bash
cd frontend
npm install
npm start
```

---

##  Environment Variables

Create `.env` inside **backend/**

```
HF_TOKEN=your_huggingface_token_here
```

---

##  AWS Deployment

*  Frontend hosted on **S3 Static Website**
*  Distributed via **CloudFront**
*  Backend deployed on **EC2**
*  Public API exposed with proper CORS
*  Secrets managed via environment variables

---

##  Future Enhancements

* 🔹 Streaming responses
* 🔹 Chat history persistence (DynamoDB)
* 🔹 Authentication (Cognito)
* 🔹 Bedrock integration
* 🔹 Docker containerization
* 🔹 CI/CD pipeline

---

##  Author

**Amitha Chowdary**
AWS Cloud Engineer | Generative AI Enthusiast

---

⭐ If you found this project useful, consider starring the repo!
