from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def get_string_db():
  return 'sqlite:///db/weather-sqlite.db'

SQLALCHEMY_DATABASE_URL = get_string_db()

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from models.core import *

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()