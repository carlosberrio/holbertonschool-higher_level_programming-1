#!/usr/bin/python3
"""State Model
Module that defines the ORM State Class, defines table 'states',
and sets class properties / relationship: relationship_city
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """Defines the State Class that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete")
