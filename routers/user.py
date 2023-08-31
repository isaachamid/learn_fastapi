from fastapi import APIRouter, Query, Path, Body, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict
from db.schemas import UserBase, UserDisplay
from db import db_user
from db.database import get_db

router = APIRouter(prefix='/user', tags=['User'])

# create user
@router.post('/', response_model=UserDisplay)
def create_user(user: UserBase, db = Depends(get_db)):
    return db_user.create_user(db, user)

# get all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db = Depends(get_db)):
    return db_user.get_all_users(db)

# get user
@router.get('/{id}', response_model=UserDisplay)
def find_by_id(id:int, db = Depends(get_db)):
    return db_user.find_by_id(id, db)

# update user
@router.put('/{id}', response_model=UserDisplay)
def update_by_id(id:int, user: UserBase, db = Depends(get_db)):
    return db_user.update_by_id(id, user, db)

# delete user
@router.delete('/{id}')
def delete_by_id(id:int, db = Depends(get_db)):
    return db_user.delete_by_id(id, db)
