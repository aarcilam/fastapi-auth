from src.models.user_model import User
from src.models.role_model import Role
import bcrypt


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

    def login_user(self, email: str, password: str):
        try:
            user = User.nodes.get(email=email)
            if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
                return user
            return None
        except Exception:
            return None    

    def create_user(self, name: str, email: str, password: str):
        role = self.get_role(name="user")
        # Generating Salt
        salt = bcrypt.gensalt()
        # Hashing Password
        hash_password = bcrypt.hashpw(
            password=password.encode('utf8'),
            salt=salt
        )
        user = User(name=name, email=email, password=hash_password.decode('utf8')).save()
        user.roles.connect(role)
        
        return user

    def get_role(self, name: str):
        try:
            role = Role.nodes.get(name=name)
            if not role:
                role = Role(name=name).save()
            return role
        except Exception:
            role = Role(name=name).save()
            return role