#!usr/bin/python3
"""6. First state model
Module that defines the ORM State Class, creates table 'states',
and sets class properties
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Defines the State Class that inherits from Base"""
    # ->> rows of the states table will be mapped to State class
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
