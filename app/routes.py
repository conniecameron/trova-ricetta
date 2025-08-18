from http import HTTPStatus
from flask import Flask, request, jsonify
from app.services import *

def create_app():
    app = Flask(__name__)
    services = Services()

    #Endpoint #1 Returns all recipes
    @app.route("/recipes/all", methods=["GET"])
    def get_all_recipes():
        rl = services.repo.load_recipes_from_db()
        data = [
            {
                "id": r.id,
                "title": r.title,
                "meal_type": r.meal_type.name,
                "ingredients": [ia.ingredient.name_italian for ia in r.ingredients],
                "steps": r.steps,
            }
            for r in rl.recipes
        ]
        return jsonify(data)

    # Endpoint #2 Accepts meal_type and ingredients via JSON parameters
    @app.route("/recipes/search", methods=["POST"])
    def search_recipes():
        """
        Example request:
        POST /recipes/search
        {
            "meal_type": "dolce",
            "ingredients": ["uova", "farina", "latte"]
        }
        """
        data = request.get_json()
        meal_type = services.get_meal_type_from_input(data.get("meal_type"))
        ingredients = services.get_ingredient_objects(data.get("ingredients", []))
        matches = services.find_recipes_by_meal_and_ingredients(meal_type, ingredients)

        response = [
            {
                "id": r.id,
                "title": r.title,
                "meal_type": r.meal_type.name,
                "ingredients": [ia.ingredient.name_italian for ia in r.ingredients],
                "steps": r.steps,
            }
            for r in matches
        ]
        return jsonify(response)

    return app

if __name__ == "__main__":
    myapp = create_app()
    myapp.run(debug=True)
