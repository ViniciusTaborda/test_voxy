from pydantic import BaseModel


class WordBody(BaseModel):
    text: str
