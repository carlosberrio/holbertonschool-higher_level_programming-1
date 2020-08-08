#!/usr/bin/python3
""" 12-model_state_update_id_2
Module that connects with the hbtn_0e_6_usa database
changes the name of a State object from the database hbtn_0e_6_usa
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
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
    session.commit()
    session.close()
