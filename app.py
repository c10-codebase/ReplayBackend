from fastapi import FastAPI
from fastapi import Depends, FastAPI
from routers import user
from mongoengine import connect
from config import db

app = FastAPI()

db_conn = db.db_connection()

app.include_router(user.router)