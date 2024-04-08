# advanced_user_operations.py

from models.user import User
from database.connection import create_connection

def create_user_with_profile(username, email, age=None, gender=None, address=None):
    user = User(username, email, age, gender, address)
    user.save()

def retrieve_users_by_criteria(criteria):
    conn = create_connection('database/my_database.db')
    if conn is not None:
        cursor = conn.cursor()
        query = 'SELECT * FROM users WHERE ' + criteria
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

def update_user_profile(user_id, **kwargs):
    conn = create_connection('database/my_database.db')
    if conn is not None:
        cursor = conn.cursor()
        query = 'UPDATE users SET ' + ', '.join([f'{key} = ?' for key in kwargs.keys()]) + ' WHERE id = ?'
        cursor.execute(query, (*kwargs.values(), user_id))
        conn.commit()
        conn.close()

def delete_users_by_criteria(criteria):
    conn = create_connection('database/my_database.db')
    if conn is not None:
        cursor = conn.cursor()
        query = 'DELETE FROM users WHERE ' + criteria
        cursor.execute(query)
        conn.commit()
        conn.close()
