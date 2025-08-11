import mysql.connector
from db.interface import *


class MysqlRepository(Repository):

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',

            #Github Push
            #'host': 'mysql',  # When you run this on your machine change it to 'localhost'
            #'port': '3306',  # When you run this on your machine change it to '32000'
            #Local Machine
            'host': 'localhost',  # When you run this on your machine change it to 'localhost'
            'port': '32000',  # When you run this on your machine change it to '32000'
            'database': 'ricetta'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def load_ingredients(self):
        sql = 'SELECT COUNT(*) FROM Ingredient;'
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def check_mealtype(self):
        sql = 'SELECT DISTINCT meal_type_id FROM Recipe;'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return [row[0] for row in result]

    def __del__(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()

if __name__ == "__main__":
    try:
        repo = MysqlRepository()
        print("Successfully connected to ricetta database")
        repo.cursor.execute("SHOW TABLES;")
        print("Tables:", repo.cursor.fetchall())
    except Exception as e:
        print("Connection failed:", e)
