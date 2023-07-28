from fastapi import APIRouter
from src.utils.auth import api_validation


class WorkOut:
    def __init__(self) -> None:
        router = APIRouter(prefix="/workout")
        
        
        @router.get("/")
        @api_validation
        def get_workout(self):
            pass