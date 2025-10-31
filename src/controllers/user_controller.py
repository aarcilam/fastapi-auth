from src.services.user_service import UserService

class UserController:
    
    def create_user(self, name: str, email: str, password: str):
        user_service = UserService()
        user = user_service.create_user(name, email, password)
        return user