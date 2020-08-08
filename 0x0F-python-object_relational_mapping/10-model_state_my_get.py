#!/usr/bin/python3
""" 10-model_state_my_get
Module that connects with a (user input) database and prints the State
ID according name passed as argument from that database
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
    #  Query.first() returns the first result as a scalar (object):
    state = session.query(State).filter_by(name=argv[4]).first()
    print(state.id if state else "Not found")
    session.close()
