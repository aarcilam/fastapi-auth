from fastapi import FastAPI;
from pydantic import BaseModel;
from src.routes.auth import auth_router;

app = FastAPI(); 

app.include_router(auth_router, prefix="/auth");