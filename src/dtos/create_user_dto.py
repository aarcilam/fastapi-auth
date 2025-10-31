from pydantic import BaseModel;

class create_user_dto(BaseModel):
    name: str
    email: str
    password: str   