from fastapi import APIrouter;
from src.dtos.login_dto import login_dto;
auth_router = APIrouter();

@auth_router.post("/login")
async def login(dto: login_dto):
    return {"message": "Login successful"}