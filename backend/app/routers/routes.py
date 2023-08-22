from fastapi import APIRouter
from app.internal.word_count import word_count_regex

from app.internal.body import WordBody

router = APIRouter()


@router.post("/words/count")
def count_words(body: WordBody):
    word_count = word_count_regex(body.text)

    return {"word_count": word_count}
