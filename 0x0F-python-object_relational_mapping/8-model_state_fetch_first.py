#!/usr/bin/python3
""" 8-model_state_fetch_first.py
Module that connects with the hbtn_0e_6_usa database and
prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Generate database schema
    Base.metadata.create_all(engine)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name) if state else "Nothing")
    session.close()
