from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.routes import router

app = FastAPI()

# Allow all origins
allow_all = ["*"]

# For testing puposes only
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all,
)
app.include_router(router)
