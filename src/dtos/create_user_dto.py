from pydantic import BaseModel;
from typing import Literal

class create_user_dto(BaseModel):
    name: str
    username: str 
    phone: str | None = None
    email: str
    password: str  
    role: Literal["user", "admin"] | None = "user" 