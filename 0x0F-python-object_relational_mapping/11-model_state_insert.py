#!/usr/bin/python3
""" A module that adds the State object "Louisiana" to the database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    addloui = State(name='Louisiana')
    session.add(addloui)
    ni = session.query(State).filter_by(name='Louisiana').first()
    print(ni.id)
    session.commit()
