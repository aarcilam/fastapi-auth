from src.models.user_model import User
from src.services.user_service import UserService

class SeedUsers:
    def run(self):
        users = [
            {"username": "admin", "email": "admin@admin.com", "phone": "+573143915310", "name": "Administrator", "password": "123456789", "role": "admin"}
        ]
        for user_data in users:
            try:
                existing_user = User.nodes.filter(username=user_data["username"]).first()
            except Exception:
                existing_user = None
            if not existing_user:
                user = UserService().create_user(
                    name=user_data["name"],
                    username=user_data["username"],
                    phone=user_data["phone"],
                    email=user_data["email"],
                    password=user_data["password"],
                    role=user_data["role"]
                )
                print(f"Created user: {user.username}")
            else:
                print(f"User {user_data['username']} already exists.")