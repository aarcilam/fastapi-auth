from fastapi import APIRouter
from src.controllers.user_controller import UserController
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends
user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@user_router.get("/")
async def get_users(token: Annotated[str, Depends(oauth2_scheme)]):
    users = UserController().get_users()
    return {"users": users}