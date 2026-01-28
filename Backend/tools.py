from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")  
)

def analyze_interaction(text: str):
    prompt = f"""
    Summarize the doctor interaction in one line
    and detect sentiment (Positive / Neutral / Negative).

    Interaction:
    {text}
    """

    response = llm.invoke(prompt)

    return {
        "summary": response.content,
        "sentiment": "Positive"
    }
