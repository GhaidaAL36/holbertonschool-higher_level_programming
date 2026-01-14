#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
whose name starts with the letter 'N'.
"""

import MySQLdb
import sys


def list_states_n(username, password, database):
    """
    Connects to the MySQL database and prints all states whose
    name starts with 'N'.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database name
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_n(sys.argv[1], sys.argv[2], sys.argv[3])
