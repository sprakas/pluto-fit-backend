from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.google import router as google_auth_router
from modules.users.user_controller import router as user_router

app = FastAPI(title="Pluto Fit Backend API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080", "https://pluto-fit-chat.lovable.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(google_auth_router)
app.include_router(
    prefix="/v1/user",
    tags=["Users"],
    router=user_router
)