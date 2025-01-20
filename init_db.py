import sqlite3

# Define the database name
DATABASE = 'database.db'


# Create the database schema
def init_db():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Create the bowls table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bowls (
        bowl_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        size TEXT NOT NULL,
        material TEXT NOT NULL,
        description TEXT,
        image_url TEXT,
        unique_attributes TEXT
    );
    ''')
    # Create the users table
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           user_id INTEGER PRIMARY KEY AUTOINCREMENT,
           first_name TEXT NOT NULL,
           last_name TEXT NOT NULL,
           user_email TEXT UNIQUE NOT NULL,
           user_password TEXT NOT NULL,
           is_admin BOOLEAN NOT NULL DEFAULT 0
       );
       ''')

    # Commit changes and close connection
    connection.commit()
    connection.close()


if __name__ == "__main__":
    init_db()
    print(f"Database '{DATABASE}' initialized successfully.")
