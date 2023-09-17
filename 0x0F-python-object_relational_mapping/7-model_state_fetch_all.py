#!/usr/bin/env python3
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    Session = sessionmaker()
    engine = create_engine(
        "mysql://{}:{}@localhost/{}".format(*sys.argv[1:4]), pool_pre_ping=True
    )
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
