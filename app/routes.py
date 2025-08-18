from http import HTTPStatus
from flask import Flask, request, jsonify, render_template, send_file
from app.services import *

def create_app():
    #app = Flask(__name__)
    app = Flask(__name__, template_folder="/home/connie/PycharmProjects/trova-ricetta/web")
    services = Services()

    #Endpoint #1 Returns all recipes
    @app.route("/recipes/all", methods=["GET"])
    def get_all_recipes():
        try:
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
            #return jsonify({"recipes": data}), HTTPStatus.OK
            return jsonify(data), HTTPStatus.OK
        except Exception as e:
            return error(f"Failed to load recipes: {e}", HTTPStatus.INTERNAL_SERVER_ERROR)

    # Endpoint #2 Accepts meal_type and ingredients via JSON parameters
    @app.route("/recipes/search", methods=["POST"])
    def search_recipes():
        """
        JSON body:
        {
          "meal_type": "dolce",
          "ingredients": ["uova","farina","latte"],
        }
        """
        if not request.is_json:
            return error("Expected application/json body.", HTTPStatus.BAD_REQUEST)

        data = request.get_json(silent=True) or {}
        meal_type_raw = data.get("meal_type")
        ingredients_raw = data.get("ingredients")

        # Validate input and types
        # May remove depending on html input constraints
        if not isinstance(meal_type_raw, str) or not meal_type_raw.strip():
            return error("Field 'meal_type' must be a non-empty string.", HTTPStatus.BAD_REQUEST)

        if ingredients_raw is None or not isinstance(ingredients_raw, list) \
           or not all(isinstance(x, str) for x in ingredients_raw):
            return error("Field 'ingredients' must be a list of strings.", HTTPStatus.BAD_REQUEST)

        try:
            meal_type = services.get_meal_type_from_input(meal_type_raw)
        except ValueError as ve:
            return error(str(ve), HTTPStatus.BAD_REQUEST)

        try:
            ingredients = services.get_ingredient_objects(ingredients_raw)
            matches = services.find_recipes_by_meal_and_ingredients(
                meal_type, ingredients
            )

            if not matches:
                return error("Nessuna ricetta trovata.", HTTPStatus.NOT_FOUND)

            # Success payload
            payload = [
                {
                    "id": r.id,
                    "title": r.title,
                    "meal_type": r.meal_type.name,
                    "match_count": len(set([i.name_italian for i in ingredients]) & set(r.get_ingredient_names())),
                    "ingredients": [ia.ingredient.name_italian for ia in r.ingredients],
                    "steps": r.steps,
                }
                for r in matches
            ]
            return jsonify(payload), HTTPStatus.OK

        except Exception as e:
            # Catch-all
            return error(f"Search failed: {e}", HTTPStatus.INTERNAL_SERVER_ERROR)

    # Health Check and Error handling
    def error(message: str, code: HTTPStatus):
        resp = jsonify({"error": {"code": code, "message": message}})
        return resp, code

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), HTTPStatus.OK

    # HTML integration
    @app.route("/ingredients", methods=["GET"])
    def ingredients():
        rl = services.repo.load_recipes_from_db()
        names = sorted({
            ia.ingredient.name_italian
            for r in rl.recipes
            for ia in r.ingredients
        })
        return jsonify({"ingredients": names}), HTTPStatus.OK

    @app.route("/docs/search", methods=["GET"])
    def docs_search():
        return render_template("trova_ricetta.html")
        #return send_file("/home/connie/PycharmProjects/trova-ricetta/web/trova_ricetta.html")

    return app

if __name__ == "__main__":
    myapp = create_app()
    myapp.run(debug=True)
