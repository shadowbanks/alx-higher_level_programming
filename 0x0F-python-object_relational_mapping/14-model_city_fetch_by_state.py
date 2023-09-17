#!/usr/bin/env python3
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:4]), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    main()
