#!/usr/bin/python3
"""A module that prints the first State object from the database"""

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

    fstate = session.query(State).order_by(State.id).first()
    if fstate:
        print("{}: {}".format(fstate.id, fstate.name))
    else:
        print("Nothing")

    session.close()
