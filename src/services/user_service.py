from src.models.user_model import User


class UserService:
    """Service for user operations using the neomodel User model.

    This keeps things simple by delegating persistence to neomodel's
    StructuredNode API (used in `src/models/user_model.py`).
    """

    def __init__(self):
        pass

    def get_user(self, user_id: str):
        try:
            return User.nodes.get(uid=user_id)
        except Exception:
            return None

    def get_users(self):
        return User.nodes.all()        

    def create_user(self, name: str, email: str, password: str):
        user = User(name=name, email=email, password=password).save()
        return user