from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

with open('config.json') as config_file:
    data = json.load(config_file)
    SQLALCHEMY_DATABASE_URL = data['SQLALCHEMY_DATABASE_URL']
    
Engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_table():#呼叫create table就可以創好資料表(2l)
    Base.metadata.create_all(Engine)
def drop_table():
    Base.metadata.drop_all(Engine)