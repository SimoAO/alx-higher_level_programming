#!/usr/bin/python3
"""
A module that lists all cities from a database.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])

    dbcur = db.cursor()

    dbcur.execute("SELECT cities.id, cities.name, states.name FROM \
            cities INNER JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")

    for state in (dbcur.fetchall()):
        print(state)

    dbcur.close()
    db.close()
