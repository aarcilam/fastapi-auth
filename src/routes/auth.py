from fastapi import APIRouter
from src.dtos.login_dto import login_dto
from src.dtos.create_user_dto import create_user_dto
from src.controllers.user_controller import UserController
from src.controllers.auth_controller import AuthController
auth_router = APIRouter()


@auth_router.post("/login")
async def login(dto: login_dto):
    user = AuthController().login(email=dto.email, password=dto.password)
    return {"message": "Login successful", "user": user.uid}

@auth_router.post("/register")
async def register(dto: create_user_dto):
    user = UserController().create_user(name=dto.name, email=dto.email, password=dto.password)
    return {"message": "User registered successfully", "user": user}