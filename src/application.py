from fastapi import FastAPI, Request ,HTTPException
from config.config import settings
from router import api_router
import time
from fastapi.responses import JSONResponse
from router.profilerouter import ProfileRouter
from utils.auth import api_validation

class Application:
    def __init__(self) -> None:
        app = FastAPI(title= settings.PROJECT_NAME, openapi_url= settings.OPEN_API_URL)
        
        @app.on_event('startup')
        def start_event():
            pass
        
        @app.middleware('http')
        async def middleware(request:Request, call_next):
            response = await call_next(request)
            response.headers['timestamp'] = str(time.time())
            return response
        
        @app.on_event('shutdown')
        def shutdown_event():
            pass
        
        @app.exception_handler(HTTPException)
        def Exception_handler(req:Request, exception: HTTPException):
            return JSONResponse(content={"detail": str(exception.detail)}, status_code=exception.status_code)
        
        
        
        profile_router = ProfileRouter()
        app.include_router(profile_router.router)
        #app.include_router(api_router,prefix=settings.API_V1_STR,dependencies=[api_validation])
        self.app=app