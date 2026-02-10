from sqlalchemy import Column, Integer, String
from database import Base

class InteractionModel(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
