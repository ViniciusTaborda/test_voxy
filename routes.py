import re

from fastapi import FastAPI

from app import app
from body import WordBody

app = FastAPI()


@app.post("/words/count")
def count_words(body: WordBody):
    word_count = len(re.findall(r"\w+", body.text))

    return {"word_count": word_count}
