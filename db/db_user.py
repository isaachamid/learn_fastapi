from sqlalchemy.orm.session import Session
from db.schemas import UserBase
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
    user = DbUser(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def find_by_id(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    return user


def delete_by_id(id: int, db: Session):
    user = find_by_id(id, db)
    db.delete(user)
    db.commit()
    return 'User Deleted'


def update_by_id(id: int, request: UserBase, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password),
    })
    db.commit()
    user = find_by_id(id, db)
    return user
