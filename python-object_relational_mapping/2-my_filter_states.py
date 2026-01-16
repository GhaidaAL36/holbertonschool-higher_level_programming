#!/usr/bin/python3
"""
Displays all states from the database hbtn_0e_0_usa
where the name matches the provided argument exactly.
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
