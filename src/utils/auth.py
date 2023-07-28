from functools import wraps
from fastapi import Request, HTTPException
from jose import jwt, JWTError
from config.config import settings

def api_validation(func):
    @wraps(func)
    async def wrapper(*args, request:Request, **kwargs):
        is_valid = validate_request(request.headers)
        if not is_valid:
            raise HTTPException(status_code= 400, detail= " Token validation Failed ")
        return func(*args, request, **kwargs)
    return wrapper

def validate_request(headers):
    try:
        token = headers['Authorization']
        jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return True
    except JWTError:
        return False

def create_jwt_token(payload: dict):
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

def verfiy_jwt_token(token):
    token = jwt.decode(token, settings.SECRET_KEY)
    return token