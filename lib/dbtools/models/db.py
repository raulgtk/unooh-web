# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from conf.settings import DB_URI

engine = create_engine(DB_URI, convert_unicode=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
session = scoped_session(Session)

Model = declarative_base()