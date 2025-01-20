import sqlite3

class User:
    def __init__(self, first_name, last_name, user_email, user_password, is_admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.is_admin = is_admin

    def save_to_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO users (first_name, last_name, user_email, user_password, is_admin)
        VALUES (?, ?, ?, ?, ?)
        ''', (self.first_name, self.last_name, self.user_email, self.user_password, self.is_admin))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_users():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        connection.close()
        return [User(*row[1:]) for row in rows]  # Skip `user_id` in the returned data

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.user_email})'
