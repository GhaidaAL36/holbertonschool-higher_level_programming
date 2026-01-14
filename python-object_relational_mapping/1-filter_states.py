#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
with a name starting with the letter 'N'.
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to the MySQL server and prints all states
    from the specified database whose names start with 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Fetch all results and print them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()


# Ensure code only runs when executed directly
if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
