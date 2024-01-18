#!/usr/bin/python3
"""
Script to print the first State object from the hbtn_0e_6_usa database.
Usage: ./8-model_state_fetch_first.py
<mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a connection to the MySQL database using SQLAlchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first State object and print its details
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")  # If no State object is found, print "Nothing"
    else:
        print("{}: {}".format(state.id, state.name))
