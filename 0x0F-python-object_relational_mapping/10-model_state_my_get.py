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
    search = "{}".format(sys.argv[4])
    states = (
        session.query(State)
        .filter(State.name == "{}".format(search))
        .order_by(State.id)
        .first()
    )

    if states:
        print(states.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
