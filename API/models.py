# from typing import Optional
# from uuid import UUID, uuid4
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email = str
    favorite_league = str
    content = str
    is_active = bool
    is_staff = bool
