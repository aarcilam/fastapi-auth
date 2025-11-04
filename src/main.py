from fastapi import FastAPI;
from pydantic import BaseModel;
from src.routes.auth import auth_router;
from src.routes.user import user_router;
from src.routes.role import role_router;
from neomodel import config
from src.config.settings import settings
from src.seeders.seed_users import SeedUsers
from src.seeders.seed_capacities import SeedCapacities

config.DATABASE_URL = settings.database_url

app = FastAPI()

SeedUsers().run()
SeedCapacities().run()

app.include_router(auth_router, prefix="/auth", tags=["auth"] )
app.include_router(user_router, prefix="/users", tags=["users"] )
app.include_router(role_router, prefix="/roles", tags=["roles"] )