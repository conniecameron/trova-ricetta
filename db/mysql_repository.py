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

    def load_ricetta(self):
        pass

    def __del__(self):
        self.connection.close()
