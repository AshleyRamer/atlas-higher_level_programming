#!/usr/bin/python3
""" Script that joines two tables, cities and states """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ code for script """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                FROM cities c \
                INNER JOIN states s \
                on c.state_id = s.id")
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))
