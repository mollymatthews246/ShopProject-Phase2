import sqlite3
class Bowl:
    def __init__(self, bowl_id, name, price, size, material, description, image_url, unique_attributes):
        self.bowl_id = int(bowl_id) if bowl_id else None
        self.name = name
        self.price = price
        self.size = size
        self.material = material
        self.description = description
        self.image_url = image_url
        self.unique_attributes = unique_attributes

    @staticmethod
    def get_all_bowls():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM bowls')
        rows = cursor.fetchall()
        connection.close()
        return [Bowl(*row) for row in rows]

    def save_to_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO bowls (name, price, size, material, description, image_url, unique_attributes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.name, self.price, self.size, self.material, self.description, self.image_url, self.unique_attributes))

        connection.commit()
        connection.close()