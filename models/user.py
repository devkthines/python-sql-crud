# models/user.py

from database.connection import create_connection

class User:
    def __init__(self, username, email, age=None, gender=None, address=None):
        self.username = username
        self.email = email
        self.age = age
        self.gender = gender
        self.address = address

    def save(self):
        conn = create_connection('database/my_database.db')
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, age, gender, address) VALUES (?, ?, ?, ?, ?)',
                           (self.username, self.email, self.age, self.gender, self.address))
            conn.commit()
            conn.close()
