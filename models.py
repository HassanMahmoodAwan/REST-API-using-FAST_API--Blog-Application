# from .database import Base
from __init__ import database
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

Base = database.Base

class Blog(Base):
    __tablename__ = 'create_blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    

class User(Base):
    __tablename__ = 'User Registeration'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password= Column(String)