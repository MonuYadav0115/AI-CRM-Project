import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("GROQ_API_KEY"))





#  Load API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print(" Warning: GROQ_API_KEY not found. Using fallback AI responses only.")
    llm = None
else:
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.1-8b-instant",
        temperature=0.2
    )

def analyze_interaction(text: str):
    """
    Analyze a customer interaction using Groq AI.
    Returns a dict with keys: summary, sentiment.
    If AI fails, returns a safe fallback.
    """
    # fallback response
    result = {
        "summary": "AI error",
        "sentiment": "Neutral"
    }

    # Only call AI if API key is present
    if llm:
        prompt = f"""
Analyze the following customer interaction.

Return EXACTLY in this format:
Summary: <one or two line professional summary>
Sentiment: <Positive | Negative | Neutral>

Interaction:
{text}
"""
        try:
            response = llm.invoke(prompt).content.strip()
            summary = "AI error"
            sentiment = "Neutral"

            for line in response.splitlines():
                if line.lower().startswith("summary"):
                    summary = line.split(":", 1)[1].strip()
                if line.lower().startswith("sentiment"):
                    sentiment = line.split(":", 1)[1].strip()

            result = {
                "summary": summary,
                "sentiment": sentiment
            }
        except Exception as e:
            # fallback in case of API error
            print(f" AI call failed: {e}")

    return result
