#!/usr/bin/python3
"""
A module that prints all City objects from the database
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    addci = session.query(City, State).join(State)
    for city, state in addci:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
