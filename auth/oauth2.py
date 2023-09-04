from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from db.database import get_db
from db.db_user import find_by_username
from sqlalchemy.orm.session import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = 'da2ea6d6619e238c4fdd1b7eeae50069d3af82352576dd9e4df6e77671262bf7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp' : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str=Depends(oauth2_scheme), db: Session = Depends(get_db)):
    error_credentials = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Credentials', headers={'WWW-authenticate' : 'bearer'})
    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        if not username:
            raise error_credentials
    except JWTError:
        raise error_credentials
    
    user = get_current_user(username, db)
    return user