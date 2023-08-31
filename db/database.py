from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/db_file.db', connect_args={'check_same_thread': False})
Base = declarative_base()

sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()