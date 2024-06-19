#!/usr/bin/python3
""" Script that prints all values in table states with name = arg4 """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ code for script """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    arg_list = argv[4].split()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
                 ORDER BY id ASC".format(arg_list[0]))
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))
