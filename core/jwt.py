from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from core.config import JWT_SECRET
import time

ALGORITHM = "HS256"

auth_scheme = HTTPBearer()

def verify_jwt_token(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = decode_jwt_token(token.credentials)
    user_email: str = payload.get("email")
    if user_email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return {"email": user_email}

def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

def create_jwt_token(email: str, expires_in: int = 86400):
    payload = {
        "email": email,
        "exp": time.time() + expires_in # default 24 hours expiration
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    return token