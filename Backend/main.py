from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import InteractionModel
from schemas import Interaction
from tools import analyze_interaction
import models
from fastapi.middleware.cors import CORSMiddleware  # <- add this

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- Add CORS middleware ---
origins = ["http://localhost:5173"]  # Frontend URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DB Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Existing backend routes ---
@app.post("/log-interaction")
def log_interaction(data: Interaction, db: Session = Depends(get_db)):
    ai_result = analyze_interaction(data.text)

    new_interaction = InteractionModel(
        text=data.text,
        summary=ai_result["summary"],
        sentiment=ai_result["sentiment"]
    )

    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    return new_interaction

@app.get("/interactions")
def get_interactions(db: Session = Depends(get_db)):
    return db.query(InteractionModel).all()

# --- Test route for frontend integration ---
@app.get("/api/message")
def get_message():
    return {"message": "Hello from FastAPI backend!"}


# deleted code start 
@app.delete("/interactions")
def delete_all_interactions(db: Session = Depends(get_db)):
    db.query(InteractionModel).delete()
    db.commit()
    return {"message": "All interactions deleted successfully"}
