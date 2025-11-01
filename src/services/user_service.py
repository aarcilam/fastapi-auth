from src.models.user_model import User
from src.models.role_model import Role
import bcrypt
import jwt
from src.config.settings import settings
from src.models.login_attempt_model import LoginAttempt
from src.models.session_model import Session
from datetime import datetime, timedelta


class UserService:
    def __init__(self):
        pass

    def get_user(self, user_id: str):
        try:
            return User.nodes.get(uid=user_id)
        except Exception:
            return None

    def get_users(self):
        return User.nodes.all()    

    def login_user(self, email: str, password: str, ip_address: str):
        try:
            user = User.nodes.get(email=email)
            if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
                now = datetime.utcnow()
                access_exp = now + timedelta(minutes=settings.access_token_expire_minutes)
                refresh_exp = now + timedelta(days=settings.refresh_token_expire_days)

                access_payload = {
                    "sub": user.uid,
                    "iat": int(now.timestamp()),
                    "exp": int(access_exp.timestamp()),
                }
                refresh_payload = {
                    "sub": user.uid,
                    "iat": int(now.timestamp()),
                    "exp": int(refresh_exp.timestamp()),
                }

                token = jwt.encode(access_payload, settings.secret_key, algorithm="HS256")
                refresh_token = jwt.encode(refresh_payload, settings.secret_key, algorithm="HS256")
                session = Session(token=token, created_at=now.isoformat()).save()
                user.sessions.connect(session)
                return {"token": token, "refresh_token": refresh_token}
            return None
        except Exception:
            login_attempt = LoginAttempt(timestamp="now", ip_address=ip_address).save()
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