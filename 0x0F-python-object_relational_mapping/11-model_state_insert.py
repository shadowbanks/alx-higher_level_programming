#!/usr/bin/env python3
"""
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    Session = sessionmaker()
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(*sys.argv[1:4]), pool_pre_ping=True)
    Session.configure(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.flush()
    print(new_state.id)
    session.commit()

if __name__ == '__main__':
    main()
