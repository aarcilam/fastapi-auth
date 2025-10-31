from fastapi import APIRouter
from src.dtos.login_dto import login_dto
from src.dtos.create_user_dto import create_user_dto
from src.services.user_service import UserService
auth_router = APIRouter()


@auth_router.post("/login")
async def login(dto: login_dto):
    return {"message": "Login successful"}

@auth_router.post("/register")
async def register(dto: create_user_dto):
    user_service = UserService()
    user = user_service.create_user(name=dto.name, email=dto.email, password=dto.password)
    return {"message": "User registered successfully", "user": user}