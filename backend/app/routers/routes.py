import re

from fastapi import APIRouter

from backend.app.internal.body import WordBody

router = APIRouter()


@router.post("/words/count")
def count_words(body: WordBody):
    word_count = len(re.findall(r"\w+", body.text))

    return {"word_count": word_count}
