from fastapi import APIRouter
from models import *
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from jwt import *
from fastapi.security import OAuth2PasswordBearer,JWTBearer

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register")
async def register_user(name : str , email: str, password: str,mobile: int):
    user_data_check = User_data.objects(email=email,password=password).first()
    if user_data_check:
        return JSONResponse({"message": "User already exists"},status_code=400)
    else:
        user = User_data(
            name = name,
            email=email, 
            password=password,
            mobile = mobile
            )
        user.save()
    return JSONResponse({"message": "User registered successfully"},status_code=201)

@router.post("/login")
async def login(email: str, password: str):
    user = User_data.objects(email=email).first()
    if user is None:
        return JSONResponse({"message": "Invalid username"},status_code=400)
    elif str(user.password) != str(password):
        return JSONResponse({"message": "Invalid password"},status_code=400)
    else:
        data = {
            "user_id":str(user.id),
        }
        token = create_access_token(data ,expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return JSONResponse({"message": "Login successful","token":token})

