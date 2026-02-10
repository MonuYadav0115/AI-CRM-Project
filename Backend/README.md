# AI-First CRM – HCP Interaction Module

##  Overview
This project is an AI-first CRM module designed for Life Sciences field representatives to log and analyze interactions with Healthcare Professionals (HCPs).

The system supports structured interaction logging and AI-powered summarization using LLMs.

---

##  Tech Stack

### Frontend
- React
- Redux
- CSS
- Google Inter Font

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite (can be replaced with PostgreSQL/MySQL)

### AI
- Groq LLM (llama-3.3-70b-versatile)
- LangChain
- LangGraph (Agent-based architecture)

---

##  LangGraph AI Agent

The LangGraph agent manages the full lifecycle of HCP interactions:
- Accepts raw interaction text
- Routes requests to tools
- Maintains interaction state
- Enhances CRM intelligence

---

##  LangGraph Tools (5)

1. **Log Interaction Tool**
   - Stores HCP interaction data
   - Uses LLM to summarize conversation

2. **Edit Interaction Tool**
   - Allows modification of previously logged interactions

3. **Summarize Interaction Tool**
   - Generates concise AI summaries

4. **Sentiment Detection Tool**
   - Detects Positive / Neutral / Negative sentiment

5. **Entity Extraction Tool**
   - Extracts doctor name, drug name, interest level

---

##  Frontend Features

- Log Interaction Screen
- Structured form for interaction input
- API integration with backend
- Displays saved interactions

---

##  API Endpoints

### POST /log-interaction
Logs a new HCP interaction with AI summary and sentiment.

### GET /interactions
Fetches all logged interactions.

---

##  How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
