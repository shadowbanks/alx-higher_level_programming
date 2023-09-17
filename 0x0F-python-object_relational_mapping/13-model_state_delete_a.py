#!/usr/bin/python3
"""
Module Doc
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def main():
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:4]), pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    session = Session()
    delStates = session.query(State).filter(State.name.like("%a%")).all()

    for state in delStates:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    main()
