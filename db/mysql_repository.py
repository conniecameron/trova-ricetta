import mysql.connector

from app.trova_ricetta import *
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
        #self.cursor = self.connection.cursor()
        self.cursor = self.connection.cursor(dictionary=True)

    def load_ingredients(self):
        sql = 'SELECT COUNT(*) FROM Ingredient;'
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def check_mealtype(self):
        sql = 'SELECT DISTINCT meal_type FROM Recipe;'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return [row["meal_type"] for row in result]

    def load_recipes_from_db(self) -> RecipeList:

        #Recipes
        sql = 'SELECT id, title, meal_type FROM Recipe ORDER BY id;'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        recipes = {row["id"]: row for row in result}

        #Ingredients per recipe
        sql = """SELECT ri.recipe_id, i.name_italian AS name, ri.quantity 
                 FROM RecipeIngredient ri JOIN Ingredient i ON i.id = ri.ingredient_id
                 ORDER BY ri.recipe_id, i.name_italian;"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        ing_map = {}
        for row in result:
            ing_map.setdefault(row["recipe_id"], []).append(
                IngredientAmount(Ingredient(row["name"]), row["quantity"])
        )

        #Steps per recipe
        sql = """SELECT recipe_id, step_number, text
            FROM RecipeStep
            ORDER BY recipe_id, step_number;"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        step_map = {}
        for row in result:
            step_map.setdefault(row["recipe_id"], []).append(row["text"])

        # Assemble objects
        recipe_list = RecipeList()
        for rid, r in recipes.items():
            recipe_list.add_recipe(
                Recipe(
                    id=rid,
                    title=r["title"],
                    meal_type=MealType[r["meal_type"]],
                    ingredients=ing_map.get(rid, []),
                    steps=step_map.get(rid, []),
                )
            )
        return recipe_list

    def __del__(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()

if __name__ == "__main__":
    try:
        repo = MysqlRepository()
        print("Successfully connected to ricetta database")
        repo.cursor.execute("SHOW TABLES;")
        print("Tables:\n", repo.cursor.fetchall())
        repo.cursor.execute("SELECT * FROM Ingredient;")
        print("Ingredients:\n", repo.cursor.fetchall())
        repo.cursor.execute("SELECT * FROM Recipe LIMIT 5;")
        print("Recipes:\n", repo.cursor.fetchall())

    except Exception as e:
        print("Connection failed:", e)
