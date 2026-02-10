from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


from database import SessionLocal, engine
import models
from models import InteractionModel
from schemas import Interaction, InteractionResponse
from tools import analyze_interaction

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRM Backend")

# CORS (React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Log interaction
@app.post("/log-interaction", response_model=InteractionResponse)
def log_interaction(data: Interaction, db: Session = Depends(get_db)):
    ai_result = analyze_interaction(data.text)

    interaction = InteractionModel(
        text=data.text,
        summary=ai_result["summary"],
        sentiment=ai_result["sentiment"],
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction

# Get all interactions
@app.get("/interactions", response_model=list[InteractionResponse])
def get_interactions(db: Session = Depends(get_db)):
    return db.query(InteractionModel).all()

# Delete all interactions
@app.delete("/interactions")
def delete_all_interactions(db: Session = Depends(get_db)):
    db.query(InteractionModel).delete()
    db.commit()
    return {"message": "All interactions deleted successfully"}
