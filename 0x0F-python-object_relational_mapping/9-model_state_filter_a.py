#!/usr/bin/python3
""" 9-model_state_filter_a
Module that connects with a (user input) database and lists all
State objects that contain the letter 'a' from that database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).\
            filter(State.name.ilike('%a%')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
