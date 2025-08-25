from app.services import *

services = Services()
#repo = MysqlRepository()

def test_recipe_finder():
    meal_type = services.get_meal_type_from_input("dolce")
    ingredients = services.get_ingredient_objects(["uova", "farina", "latte"])

    '''Single matching recipe'''
    matches = services.find_recipes_by_meal_and_ingredients(meal_type, ingredients)
    #checks that it returns a List:Recipe
    assert isinstance(matches, List)
    # checks that matching recipe is returned
    assert [r.title for r in matches] == ["Torta Margherita"]
    out = services.format_recipe_results(matches)
    assert out == "1) 01 — Torta Margherita [DOLCE] — 5 ingredienti"

    '''Multiple matching recipes'''
    meal_type = services.get_meal_type_from_input("secondo")
    ingredients = services.get_ingredient_objects(["cipolla", "parmigiano", "olio d'oliva"])
    matches = services.find_recipes_by_meal_and_ingredients(meal_type, ingredients)
    # checks that multiple matching recipes are returned
    assert len(matches) == 2

    '''No matching recipe'''
    meal_type = services.get_meal_type_from_input("dolce")
    ingredients = services.get_ingredient_objects(["cipolla", "farina", "latte"])
    matches = services.find_recipes_by_meal_and_ingredients(meal_type, ingredients)
    assert [r.title for r in matches] == []
    out = services.format_recipe_results(matches)
    assert out == "Nessuna ricetta trovata."





