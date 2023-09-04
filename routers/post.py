from fastapi import APIRouter, Query, Path, Body, Depends, status
from pydantic import BaseModel
from typing import Optional, List, Dict
from db.schemas import PostBase, PostDisplay
from db import db_post
from db.database import get_db
from fastapi.exceptions import HTTPException

router = APIRouter(prefix='/post', tags=['Post'])

image_url_types = ['url', 'uploaded']

# create post
@router.post('/', response_model=PostDisplay)
def create_post(post: PostBase, db=Depends(get_db)):
    if post.image_url_type not in image_url_types:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, description='image url type not valid!')
    return db_post.create_post(db, post)
