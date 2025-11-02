from fastapi import APIRouter, Cookie, HTTPException
from src.dtos.login_dto import login_dto
from src.dtos.create_user_dto import create_user_dto
from src.controllers.user_controller import UserController
from src.controllers.auth_controller import AuthController
from typing import Annotated

auth_router = APIRouter()

@auth_router.post("/login")
async def login(dto: login_dto):
    response = AuthController().login(username=dto.username, password=dto.password, ip_address=dto.ip_address)
    return {"message": "Login successful", "token": response}

@auth_router.post("/register")
async def register(dto: create_user_dto):
    user = UserController().create_user(name=dto.name, username=dto.username, phone=dto.phone, email=dto.email, password=dto.password)
    return {"message": "User registered successfully", "user": user}

@auth_router.get("/refresh-token")
async def refresh_token(refresh_token: Annotated[str, Cookie()] = None):
    print("Refresh token received:", refresh_token)
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Refresh token not provided")
    return {"message": "Token refreshed successfully", "token": AuthController().refresh_token(refresh_token)}