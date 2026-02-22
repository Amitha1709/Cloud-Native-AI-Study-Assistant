import re
import time
from duckduckgo_search import DDGS
from rag import get_answer_from_notes


# 🔢 Calculator Tool
def calculator_tool(query: str):
    try:
        expression = re.sub(r"[^0-9+\-*/().]", "", query)
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "Invalid mathematical expression."


# 🌐 Search Tool (Safe)
def search_tool(query: str):
    try:
        time.sleep(1)  # prevent rate limit
        with DDGS() as ddgs:
            results = [r["body"] for r in ddgs.text(query, max_results=2)]
        return " ".join(results)
    except:
        return "Search service temporarily unavailable. Please try again later."


# 📚 Study Tool
def study_tool(query: str):
    return get_answer_from_notes(query)