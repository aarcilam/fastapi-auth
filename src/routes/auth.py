from fastapi import APIRouter, HTTPException, Cookie
from src.dtos.login_dto import login_dto
from src.dtos.create_user_dto import create_user_dto
from src.controllers.user_controller import UserController
from src.controllers.auth_controller import AuthController
from typing import Annotated
from src.models.refresh_token_cookie_model import RefreshTokenCookie
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from pydantic import BaseModel

auth_router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    response = AuthController().login(username=form_data.username, password=form_data.password, ip_address="0.0.0.0")
    return Token(access_token=response["token"], token_type="bearer")

@auth_router.post("/login")
async def login(dto: login_dto):
    response = AuthController().login(username=dto.username, password=dto.password, ip_address=dto.ip_address)
    return {"message": "Login successful", "access_token": response["token"], "token_type": "bearer", "refresh_token": response["refresh_token"]}

@auth_router.post("/register")
async def register(dto: create_user_dto):
    user = UserController().create_user(name=dto.name, username=dto.username, phone=dto.phone, email=dto.email, password=dto.password, role=dto.role)
    return {"message": "User registered successfully", "user": user}

@auth_router.get("/refresh-token")
async def refresh_token(cookies: Annotated[RefreshTokenCookie, Cookie()]):
    print("Refresh token received:", cookies.refresh_token)
    return {"message": "Token refreshed successfully", "token": AuthController().refresh_token(cookies.refresh_token)}