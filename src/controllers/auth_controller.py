from src.services.user_service import UserService

class AuthController:
    def login(self, email: str, password: str):
        user = UserService().login_user(email, password)
        if not user:
            return {"error": "Invalid credentials"}, 401
        return user