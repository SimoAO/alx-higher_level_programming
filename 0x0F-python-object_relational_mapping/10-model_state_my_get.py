#!/usr/bin/python3
"""
A module that prints the State object with the name passed as
argument from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), 
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    pstate = session.query(State).\
            filter(State.name.like(sys.argv[4])).first()
    if pstate:
        print("{}".format(pstate.id))
    else:
        print("Not found")

    session.close()
