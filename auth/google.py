from core.jwt import create_jwt_token
from fastapi import APIRouter, HTTPException
from modules.users.user_entity import user_entity
from pydantic import BaseModel
import httpx
from jose import jwt
import time
from core.config import GOOGLE_CLIENT_ID, JWT_SECRET
from core.db import users
from fastapi import Header

router = APIRouter()


class Token(BaseModel):
    token: str

@router.post("/api/auth/google")
async def google_login(request: Token):
    token = request.token

    # 1. Verify access token with Google
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://www.googleapis.com/oauth2/v3/tokeninfo",
            params={"access_token": token},
        )
    if r.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid access token")

    token_info = r.json()

    # Verify audience
    if token_info.get("aud") != GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=401, detail="Access token not valid for this client")

    email = token_info.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Email not available in token info")

    # 2. Check if user exists in MongoDB
    user = users.find_one({"email": email})

    if not user:
        # Fetch profile from userinfo endpoint only for new users
        headers = {"Authorization": f"Bearer {token}"}
        async with httpx.AsyncClient() as client:
            profile_res = await client.get("https://www.googleapis.com/oauth2/v3/userinfo", headers=headers)
        if profile_res.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch profile info")
        profile = profile_res.json()
        name = profile.get("name")
        picture = profile.get("picture")
        result = users.insert_one({
            "email": email,
            "name": name,
            "picture": picture,
            "created_at": time.time()
        })
        user = users.find_one({"_id": result.inserted_id})
       
    # 3. Create app JWT for session
    app_token = create_jwt_token(email=email)

    response = user_entity(user)
    response["access_token"] = app_token
    return response

@router.get("/api/me")
async def get_current_user(Authorization: str = Header(...)):
    try:
        if not Authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid authorization header")
        token = Authorization.split(" ", 1)[1]
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        email = payload.get("email")
        user = users.find_one({"email": email})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user_entity(user)
            
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")