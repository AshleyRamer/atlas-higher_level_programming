#!/usr/bin/python3
""" Print 1st State object from given database """
from model_state import Base, State
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

    states = session.query(State).first()
    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
