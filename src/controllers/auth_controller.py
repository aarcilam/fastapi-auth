from src.services.user_service import UserService
from fastapi import HTTPException

class AuthController:
    def login(self, email: str, password: str, ip_address: str):
        response = UserService().login_user(email= email, password= password, ip_address= ip_address)
        if not response:
            raise HTTPException(status_code=404, detail="Something goes wrong")
        return response

    def refresh_token(self, refresh_token: str):
        response = UserService().refresh_token(refresh_token= refresh_token)
        if not response:
            raise HTTPException(status_code=404, detail="Something goes wrong")
        return response