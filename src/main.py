from fastapi import FastAPI;
from pydantic import BaseModel;
from src.routes.auth import auth_router;
from src.routes.user import user_router;
from neomodel import config
from src.config.settings import settings

config.DATABASE_URL = settings.database_url

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"] )
app.include_router(user_router, prefix="/users", tags=["users"] )