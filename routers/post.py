import random
from fastapi import APIRouter, Query, Path, Body, Depends, status, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List, Dict
from db.schemas import PostBase, PostDisplay
from db import db_post
from db.database import get_db
from fastapi.exceptions import HTTPException
from string import ascii_letters
import shutil

router = APIRouter(prefix='/post', tags=['Post'])

image_url_types = ['url', 'uploaded']

# create post


@router.post('/', response_model=PostDisplay)
def create_post(post: PostBase, db=Depends(get_db)):
    if post.image_url_type not in image_url_types:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, description='image url type not valid!')
    return db_post.create_post(db, post)

# get all posts


@router.get('/', response_model=List[PostDisplay])
def get_all_posts(db=Depends(get_db)):
    return db_post.get_all_posts(db)

# upload file
@router.post('/upload_file')
def upload_file(file: UploadFile = File(...)):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f'_{rand_str}.'.join(file.filename.rsplit('.', 1))
    path = f'uploads/{new_name}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        'path': path
    }

# get post
@router.get('/{id}', response_model=PostDisplay)
def find_by_id(id: int, db=Depends(get_db)):
    return db_post.find_by_id(id, db)

# update post
@router.put('/{id}', response_model=PostDisplay)
def update_by_id(id: int, user: PostBase, db=Depends(get_db)):
    return db_post.update_by_id(id, user, db)

# delete post
@router.delete('/{id}')
def delete_by_id(id: int, db=Depends(get_db)):
    return db_post.delete_by_id(id, db)
