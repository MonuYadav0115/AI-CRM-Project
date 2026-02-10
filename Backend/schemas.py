from pydantic import BaseModel

class Interaction(BaseModel):
    text: str

class InteractionResponse(BaseModel):
    id: int
    text: str
    summary: str
    sentiment: str

    class Config:
        from_attributes = True
