from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.google import router as google_auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080", "https://pluto-fit-chat.lovable.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(google_auth_router)
