from fastapi import FastAPI

from app.database import Base, engine
from app.routes.games import router as games_router

Base.metadata.create_all(bind=engine)

app = FastAPI (
    title="GameVault API",
    description= "API for videogame inventory and resale management",
    version= "1.0.0"
)

app.include_router(games_router)

@app.get("/")
def root():
    return{
        "name": "GameVault API",
        "version": "1.0.0",
        "status":"online"
    }