from fastapi import APIRouter
from services.profileservice import ProfileServices
#from utils.auth import api_validation
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.profile import Profile
from services.profileservice import ProfileServices
from fastapi import Request, Body
from utils.auth import create_jwt_token,verfiy_jwt_token
from fastapi.responses import JSONResponse


class ProfileRouter:
    
    def __init__(self) -> None:
        self.router = APIRouter(prefix="/profile")
        self.service = ProfileServices()

        self.router.post("/login")(self.login_user)
        self.router.post("/register")(self.register_user)
        self.router.get("/get_user")(self.get_user)
        self.router.get("/update_user_data")(self.update_user_data)


    async def register_user(self, request: Request, register_data: dict = Body(...)):
        username = register_data.get("username")
        password = register_data.get("password")
        email = register_data.get("email")
        phone = register_data.get("phone")
        data = self.service.register_user(username, email, phone,password)
        if data == "register sucessfully":
            return JSONResponse({"message":"Register successfully"},status_code=200)
        else:
            return JSONResponse({"message":data},status_code=400)
    
    async def login_user(self,request: Request, login_data: dict = Body(...)):
        email = login_data.get("email")
        password = login_data.get("password")
        profile = self.service.login_user(email, password)
        if not profile:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        access_token = create_jwt_token(profile)
        return {"access_token": access_token, "token_type": "bearer"}
    
    async def get_user(self,request: Request):
        token = request.headers.get('Authorization', None)
        if token != None and token !='':
            blank_token =token.split('Bearer ')
            token_data = verfiy_jwt_token(blank_token[1])
            data = self.service.get_user_data(token_data)
            print(data)
        return JSONResponse(data,status_code=200)
    
    async def update_user_data(self,request: Request, data: dict = Body(...)):
        token = request.headers.get('Authorization', None)
        if token != None and token !='':
            blank_token =token.split('Bearer ')
            token_data = verfiy_jwt_token(blank_token[1])
            user_data = data
            data = self.service.user_data_update(token_data,user_data)
            if data == "update successful":
                return JSONResponse({"message":data},status_code=200)
            else:
                return JSONResponse({"message":"update unsuccessfully "},status_code=400)
    
    
        