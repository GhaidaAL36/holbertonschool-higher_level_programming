#!/usr/bin/python3
"""
This module connects to a MySQL database and displays all states
from the 'states' table where the name matches the provided argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments: username, password, database, state name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Use format to safely insert the user input into SQL query
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all matching states and print them
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
