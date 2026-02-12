import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq




load_dotenv()

# Load and clean API key
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    api_key = api_key.strip()  # remove spaces
    print("Loaded GROQ_API_KEY:", repr(api_key))
else:
    print("❌ GROQ_API_KEY not found")
    llm = None

if api_key:
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.1-8b-instant",
        temperature=0.2
    )
else:
    llm = None

def analyze_interaction(text: str):
    result = {"summary": "AI error", "sentiment": "Neutral"}
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
            result = {"summary": summary, "sentiment": sentiment}
        except Exception as e:
            print(f"AI call failed: {e}")
    return result
