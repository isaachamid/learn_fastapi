from sqlalchemy.orm import Session
from db.schemas import UserBase
from db.models import User
from db.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status

def create_user(db: Session, request: UserBase):
    user = User(
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(User).all()


def find_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    return user

def find_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found!')
    return user

def delete_by_id(id: int, db: Session):
    user = find_by_id(id, db)
    db.delete(user)
    db.commit()
    return 'User Deleted'


def update_by_id(id: int, request: UserBase, db: Session):
    user = db.query(User).filter(User.id == id)
    user.update({
        User.username: request.username,
        User.email: request.email,
        User.password: Hash.bcrypt(request.password),
    })
    db.commit()
    user = find_by_id(id, db)
    return user
