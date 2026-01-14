#!/usr/bin/python3
"""
This module connects to a MySQL database and displays all states
from the 'states' table where the name matches the provided argument.
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Connects to the MySQL database and prints all states whose
    name matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): State name to search for.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
        state_name
    )
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
