#!/usr/bin/python3
""" Delete all states with an a in their name"""
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    my_url = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(my_url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state_name, city_id, city_name in session.query(
        State.name, City.id, City.name).filter(
            City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state_name, city_id, city_name))
