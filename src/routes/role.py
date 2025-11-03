from fastapi import APIRouter
from src.controllers.role_controller import RoleController

role_router = APIRouter()

@role_router.post("/")
async def create_role(name: str):
    from src.controllers.role_controller import RoleController
    role = RoleController().create_role(name=name)
    return {"role": role}

@role_router.get("/")
async def get_roles():
    roles = RoleController().get_roles()
    return {"roles": roles}
