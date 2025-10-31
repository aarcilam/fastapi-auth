from fastapi import FastAPI;
from pydantic import BaseModel;
from src.routes.auth import auth_router;
from src.routes.user import user_router;
from neomodel import config

config.DATABASE_URL = 'bolt://neo4j:test1234@localhost:7687'

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/api")