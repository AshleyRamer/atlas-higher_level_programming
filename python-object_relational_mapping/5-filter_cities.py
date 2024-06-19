#!/usr/bin/python3
""" Script that prints all cities that are in inputted state, formatted """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ code for script """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name \
                FROM cities c \
                INNER JOIN states s \
                on c.state_id = s.id \
                WHERE s.name like BINARY %(state_name)s",
                {'state_name': argv[4]})
    rows = cur.fetchall()
    x = []
    for tup in rows:
        x.append(str(tup[0]))
    print(", ".join(x))
