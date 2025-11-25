# src/main.py


from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn
from src.config import database_settings

app = FastAPI()
Instrumentator().instrument(app).expose(app)


if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, reload=True)
