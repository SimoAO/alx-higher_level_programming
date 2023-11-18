#!/usr/bin/python3
"""
A module that takes in the name of a state as an argument and lists
all cities of that state from a database.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])

    dbcur = db.cursor()

    dbcur.execute("SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id WHERE states.name \
            LIKE BINARY %s ORDER BY cities.id ASC", (sys.argv[4], ))

    for city in (dbcur.fetchall()):
        print(", ".join(city[0]))

    dbcur.close()
    db.close()
