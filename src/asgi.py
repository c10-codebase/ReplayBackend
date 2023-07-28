import uvicorn
from application import Application


app = Application().app


if __name__ == "__main__":
    uvicorn.run(app)