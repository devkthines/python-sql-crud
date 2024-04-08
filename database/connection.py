# database/connection.py

import sqlite3

def create_connection(database_file):
    try:
        conn = sqlite3.connect(database_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None
