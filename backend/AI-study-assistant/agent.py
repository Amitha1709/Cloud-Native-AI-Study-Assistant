import re
import os
import requests
from dotenv import load_dotenv
from tools import calculator_tool, search_tool, study_tool

# ===============================
# 🔐 Load environment variables
# ===============================
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

# ✅ BEST FREE MODEL
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


# ===============================
# 🔹 HuggingFace API call
# ===============================
def generate_answer(prompt: str):
    try:
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.5
            }
        }

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )
        
        # ⭐ HANDLE MODEL LOADING 
        if response.status_code == 503: 
            return "Model is loading, please try again in 10 seconds." 
        response.raise_for_status() 
        result = response.json() 
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        return "AI could not generate response."

    except Exception as e:
        print("HF ERROR:", e)
        return "Error connecting to HuggingFace API."


# ===============================
# 🔹 Main Agent Router
# ===============================
def ask_agent(question: str):

    question_lower = question.lower().strip()

    # 🔢 Calculator
    math_pattern = r'^\s*\d+(\s*[\+\-\*/]\s*\d+)+\s*$'
    if re.match(math_pattern, question_lower):
        return calculator_tool(question)

    # 🌐 Weather / News
    if any(word in question_lower for word in ["weather", "news"]):
        return search_tool(question)

    # 📚 Academic RAG trigger
    academic_keywords = [
        "cloud", "virtualization", "infrastructure",
        "iaas", "paas", "saas", "security",
        "identity", "reputation"
    ]

    if any(word in question_lower for word in academic_keywords):
        context = study_tool(question)

        prompt = f"""
Use the context below to answer clearly in 3–4 sentences.

Context:
{context}

Question:
{question}

Answer:
"""
        return generate_answer(prompt)

    # 🤖 General AI fallback
    prompt = f"""
You are an expert cloud tutor.

Explain the following clearly in 3–4 sentences.

Question:
{question}

Answer:
"""
    return generate_answer(prompt)