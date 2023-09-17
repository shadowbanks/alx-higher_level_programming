#!/usr/bin/env python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    Session = sessionmaker()
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:4]), pool_pre_ping=True
    )
    Session.configure(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
