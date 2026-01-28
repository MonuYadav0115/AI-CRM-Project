from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class InteractionModel(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    summary = Column(String)
    sentiment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

