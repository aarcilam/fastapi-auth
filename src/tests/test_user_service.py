from src.services.user_service import UserService
from neomodel import config
from src.config.settings import settings

config.DATABASE_URL = settings.database_url

class TestUserService:
    token: str = ""
    refresh_token: str = ""

    def test_get_users(self):  
        user_service = UserService()
        users = user_service.get_users()
        print(users)
        assert isinstance(users, list)
        for user in users:
            assert hasattr(user, 'uid')
            assert hasattr(user, 'name')
            assert hasattr(user, 'email')

    def test_get_role(self):
        user_service = UserService()
        role = user_service.get_role(name="user")
        assert role is not None
        assert role.name == "user"

    def test_create_user(self):
        user_service = UserService()
        user = user_service.create_user(
            name="Test User",
            username="testuser",
            phone=None,
            email="andresarcila2@me.com",
            password="securepassword"
        )
        assert user is not None
        assert hasattr(user, 'uid')
        assert user.name == "Test User"
        assert user.username == "testuser"
        assert user.email == "andresarcila2@me.com"
    
    def test_login_user(self):
        user_service = UserService()
        login_response = user_service.login_user(
            username="testuser",
            password="securepassword",
            ip_address="0.0.0.0"
        )
        assert login_response is not None
        self.token = login_response["token"]
        self.refresh_token = login_response["refresh_token"]

    def test_refresh_token(self):
        user_service = UserService()
        refresh_token = self.refresh_token
        refresh_response = user_service.refresh_token(refresh_token=refresh_token)
        assert refresh_response is not None
        
    def test_get_user(self):
        user_service = UserService()
        users = user_service.get_users()
        if users:
            user_id = users[0].uid
            user = user_service.get_user(user_id=user_id)
            assert user is not None
            assert user.uid == user_id  