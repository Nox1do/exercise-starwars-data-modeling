import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(Integer, nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    class Planets(Base):
        __tablename__ = 'Planets'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        population = Column(Integer, nullable=False)
        climate = Column(String(250), nullable=False)
        terrain = Column(String(250), nullable=False)
        user_id = Column(Integer, ForeignKey('user.id'))
        user = relationship(User)

    class Favorites_Characters(Base):
        __tablename__ = 'Favorites-Characters'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        character_id = Column(Integer,ForeignKey('planets.id'))

    class Favorites_Planets(Base):
        __tablename__ = 'Favorites-Planets'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        planets_id = Column(Integer,ForeignKey('planets.id'))

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'starwars.png')
