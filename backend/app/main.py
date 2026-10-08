from fastapi import FastAPI 
from sqlalchemy import text

from app.api.routes.auth import router as auth_router
from app.db.session import engine

app = FastAPI(
    title="Orbe API",
    version="0.1.0",
)

app.include_router(auth_router)

@app.get("/health")
def health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status" : "ok",
        "database" : "connected papai",
    }
