#!/usr/bin/python3
""" Delete all states with an a in their name"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    my_url = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.\
                           format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
        print("State name updated successfully!")
    else:
        print("State with id 2 not found.")
    session.close()
