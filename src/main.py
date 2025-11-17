# src/main.py


from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from src.firstapp.router import router
import uvicorn
from src.config import database_settings

app = FastAPI()
Instrumentator().instrument(app).expose(app)


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, reload=True)
