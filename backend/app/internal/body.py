from pydantic import BaseModel, Field


class WordBody(BaseModel):
    text: str = Field(..., min_length=1)
