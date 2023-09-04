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
