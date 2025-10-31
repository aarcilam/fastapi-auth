from src.services.user_service import UserService
from fastapi import HTTPException

class AuthController:
    def login(self, email: str, password: str):
        response = UserService().login_user(email, password)
        if not response:
            raise HTTPException(status_code=404, detail="Something goes wrong")
        return response