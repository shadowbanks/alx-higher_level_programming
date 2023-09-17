#!/usr/bin/python3
"""
Module Doc
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    Session = sessionmaker()
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:4]),
        pool_pre_ping=True
    )
    Session.configure(bind=engine)
    session = Session()

    update = session.query(State).filter(State.id == 2).first()
    update.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    main()
