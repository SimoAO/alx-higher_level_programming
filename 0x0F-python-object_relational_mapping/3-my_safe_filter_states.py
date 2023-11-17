#!/usr/bin/python3
"""
A module that is safe from MYSQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])

    dbcur = db.cursor()

    dbcur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC", (sys.argv[4], ))

    for state in (dbcur.fetchall()):
        print(state)

    dbcur.close()
    db.close()
