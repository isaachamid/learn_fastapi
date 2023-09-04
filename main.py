from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user, post
from auth import authentication
from db import models
from db.database import engine

app = FastAPI()
# app.include_router(blog_get.router)
# app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)
app.mount('/files', StaticFiles(directory='uploads'), name='files')
models.Base.metadata.create_all(engine)


@app.get('/')
def hello():
    return 'hello world'
