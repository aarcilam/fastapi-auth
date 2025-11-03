from src.services.user_service import UserService

class UserController:
    
    def create_user(self, name: str, username: str, phone: str | None, email: str, password: str, role: str | None = "user"):
        user_service = UserService()
        user = user_service.create_user(name, username, phone, email, password, role)
        if not user:
            return None
        try:
            roles = [r.name for r in user.roles.all()]
        except Exception:
            roles = []
        return {
            "uid": user.uid,
            "name": user.name,
            "email":user.email,
            "roles": roles,
        }

    def get_users(self):
        user_service = UserService()
        users = user_service.get_users()
        result = []
        for u in users:
            try:
                roles = [r.name for r in u.roles.all()]
            except Exception:
                roles = []
            result.append({
                "uid": u.uid,
                "name": u.name,
                "email":u.email,
                "roles": roles,
            })
        return result