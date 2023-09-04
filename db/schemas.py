from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    username: str


class UserBase(BaseModel):
    username: str
    password: str
    email: str


class UserDisplay(BaseModel):
    username: str
    email: str


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
