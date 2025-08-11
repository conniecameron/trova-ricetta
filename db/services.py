import db.mysql_repository
from app.trova_ricetta import *
from typing import List

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    '''Use case 1: 
    Accepts meal category (dropdown) and 3 ingredients (checklist). 
    Returns matching Italian recipe/s.'''

    def get_meal_type_from_input(user_input: str) -> MealType:
        mapping = {
            "antipasto": MealType.ANTIPASTO,
            "primo": MealType.PRIMO,
            "secondo": MealType.SECONDO,
            "dolce": MealType.DOLCE
        }

    def get_ingredient_objects(names: List[str]) -> List[Ingredient]:
        return [Ingredient(name) for name in names]

    def find_recipes_by_meal_and_ingredients(
            meal_type: MealType,
            ingredients: List[Ingredient],
            recipes: List[Recipe]
    ) -> List[Recipe]:

        wanted = {ing.name_italian for ing in ingredients}  # Ingredient stores lowercase in your class
        matches: List[Recipe] = []
        for r in recipes:
            if r.meal_type != meal_type:
                continue
            recipe_names = set(r.get_ingredient_names())
            if wanted.issubset(recipe_names):
                matches.append(r)
        return matches

    def find_recipes_in_list(
            meal_type: MealType,
            ingredients: List[Ingredient],
            recipe_list: RecipeList
    ) -> List[Recipe]:
        """Convenience wrapper if you have a RecipeList instance."""
        return find_recipes_by_meal_and_ingredients(meal_type, ingredients, recipe_list.recipes)


