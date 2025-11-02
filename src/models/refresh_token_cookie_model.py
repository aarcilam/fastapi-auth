from pydantic import BaseModel

class RefreshTokenCookie(BaseModel):
    refresh_token: str