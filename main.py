from fastapi import FastAPI
from mongoengine import connect
from models import *
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from jwt import *

####################################################################################

app = FastAPI()
connect('medical', host='127.0.0.1', port=27017)

@app.post("/register")
def register_user(name : str , email: str, password: str,mobile: int):
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

@app.post("/login")
def login(email: str, password: str):
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