from pydantic import BaseModel;

class create_user_dto(BaseModel):
    name: str
    username: str 
    phone: str | None = None
    email: str
    password: str   