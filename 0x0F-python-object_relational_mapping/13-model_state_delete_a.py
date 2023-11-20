#!/usr/bin/python3
""" A module that lists all State objects that contain the letter a
from the database """

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from sqlalchemy.ext.declarative import declarative_base

    engine = create_engine("mysql://{}:{}@localhost/{}".
            format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    chstate = session.query(State).filter(State.name.like('%a%'))

    for state in chstate:
        session.delete(state)

    session.commit()
