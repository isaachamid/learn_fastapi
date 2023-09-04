from sqlalchemy.orm import Session
from db.schemas import PostBase
from db.models import Post
import datetime


def create_post(db: Session, request: PostBase):
    post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=request.creator_id
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_all_posts(db: Session):
    return db.query(Post).all()


def find_by_id(id: int, db: Session):
    post = db.query(Post).filter(Post.id == id).first()
    return post


def delete_by_id(id: int, db: Session):
    post = find_by_id(id, db)
    db.delete(post)
    db.commit()
    return 'Post Deleted'


def update_by_id(id: int, request: PostBase, db: Session):
    post = db.query(Post).filter(Post.id == id)
    post.update({
        Post.image_url: request.image_url,
        Post.image_url_type: request.image_url_type,
        Post.timestamp: datetime.datetime.now(),
        Post.caption: request.caption,
        Post.user_id: request.creator_id
    })
    db.commit()
    post = find_by_id(id, db)
    return post
