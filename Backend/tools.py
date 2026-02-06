from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key = ""
)

def analyze_interaction(text: str):
    prompt = f"""
    Analyze the following doctor interaction.

    1. Give a ONE LINE summary.
    2. Detect sentiment strictly as one of these words:
       Positive, Neutral, or Negative

    Respond in this exact format:
    Summary: <summary here>
    Sentiment: <Positive/Neutral/Negative>

    Interaction:
    {text}
    """

    response = llm.invoke(prompt)
    content = response.content

    summary = "N/A"
    sentiment = "Neutral"

    for line in content.split("\n"):
        if "Summary:" in line:
            summary = line.replace("Summary:", "").strip()
        if "Sentiment:" in line:
            sentiment = line.replace("Sentiment:", "").strip()

    return {
        "summary": summary,
        "sentiment": sentiment
    }

