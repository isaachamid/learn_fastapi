from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(prefix='/blog', tags=['Blog'])

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str]
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Image = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'message': 'OK', 'data': blog, 'id': id, 'version': version}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
        id: int,
        blog: BlogModel,
        comment_title: int = Query(None, title='Title Text', description='Description Text', alias='Comment Title', deprecated=True),
        content: str = Body(..., min_length=10, max_length=50, regex='^[A-Z].*'),
        v: Optional[List[str]] = Query(['1.0', '1.2', '2.0']),
        comment_id: int = Path(gt=5)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'comment_title': comment_title,
        'content': content,
        'version': v
        }
