from fastapi import FastAPI
from app.routers import review

app = FastAPI(title="CodePalAI")

app.include_router(review.router)
