from fastapi import APIRouter
from src.controllers.user_controller import UserController
user_router = APIRouter()

@user_router.get("/")
async def get_users():
    users = UserController().get_users()
    return {"users": users}