from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(prefix='/blog', tags=['Blog'])

class TypeBlogs(str, Enum):
    Type1 = 'type1'
    Type2 = 'type2'
    Type3 = 'type3'
    
@router.get('/{blog_id}/comments/{comment_id}', tags=['Comment'])
def get_comment(blog_id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog id{blog_id} comment id {comment_id} {valid=} {username}'}


@router.get('/all')
def get_blogs(page: Optional[int] = None, page_size: str = None):
    return {'message': f'{page=} - {page_size=}'}


@router.get('/{id}', status_code=status.HTTP_200_OK, tags=['Comment'], summary='Get One blog By ID', response_description='Blog Object in JSON format')
def get_blog(id: int, response: Response):
    """ 
    main description about api
    - **id** Blog ID
    - **response** Blog Object in JSON format
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'blog {id} not found!'}
    return {'message': f'blog {id}'}
