import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(Integer, nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)


class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=True)
    gender = Column(String(250), nullable=True)
    character_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(User)


    class Planets(Base):
        __tablename__ = 'Planets'
        id =  Column(Integer, primary_key=True)
        name = Column(String(250), nullable=True)
        population = Column(Integer, nullable=True)
        climate = Column(String(250), nullable=True)
        terrain = Column(String(250), nullable=True)
        planet_id = Column(Integer, ForeignKey('users.id'))
        users = relationship(User)
     
    class Favorites(Base):
       __tablename__ = 'Favorites'
       id = Column(Integer, primary_key=True)
       character_name = Column(String(250), nullable=True)
       gplanet_name = Column(String(250), nullable=True)
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'starwars.png')