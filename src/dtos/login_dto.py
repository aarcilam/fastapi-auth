from pydantic import BaseModel;

class login_dto(BaseModel):
    email: str
    password: str   
    ip_address: str