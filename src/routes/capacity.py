from fastapi import APIRouter
from src.controllers.capacity_controller import CapacityController

capacity_router = APIRouter()   

@capacity_router.post("/")
async def create_capacity(name: str, description: str):
    from src.controllers.capacity_controller import CapacityController
    capacity = CapacityController().create_capacity(name=name, limit=description)
    return {"capacity": capacity}