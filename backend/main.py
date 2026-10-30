from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="CineBook API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "cinebook-api"}

# Routers will be included here later
# from routers import auth, movies, theatres, shows, bookings, reports
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# ...
