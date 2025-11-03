from pydantic import BaseModel;

class login_dto(BaseModel):
    username: str
    password: str   
    ip_address: str | None = None