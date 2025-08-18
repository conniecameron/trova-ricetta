import db.mysql_repository
from app.trova_ricetta import *
from typing import List

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    '''Use case 1: 
    Accepts meal category (dropdown) and 3 ingredients (checklist). 
    Returns matching Italian recipe/s.'''

    def get_meal_type_from_input(self, user_input: str) -> MealType:
        mapping = {
            "antipasto": MealType.ANTIPASTO,
            "primo": MealType.PRIMO,
            "secondo": MealType.SECONDO,
            "dolce": MealType.DOLCE
        }
        key = user_input.strip().lower()
        if key not in mapping:
            raise ValueError(f"Unknown meal type: {user_input}")
        return mapping[key]

    def get_ingredient_objects(self, names: List[str]) -> List[Ingredient]:
        return [Ingredient(name) for name in names]

    # ALL ingredients must be present on the recipe
    def find_recipes_by_meal_and_ingredients(
            self,
            meal_type: MealType,
            ingredients: List[Ingredient],
            min_matches: int = 3, #only 3 ingredients to match a recipe
    ) -> List[Recipe]:

        # pulls the recipe list straight from MySQL db
        recipe_list = self.repo.load_recipes_from_db()
        recipes = recipe_list.recipes

        wanted = {ing.name_italian for ing in ingredients}
        threshold = min(min_matches, len(wanted))  # if user provided <3, require all provided

        matches: List[Recipe] = []
        for r in recipes:
            if r.meal_type != meal_type:
                continue
            recipe_names = set(r.get_ingredient_names())
            overlap = len(wanted & recipe_names)
            if overlap >= threshold:
                matches.append(r)
        return matches

    #Convert the list of Recipe objects into a presentable format, error message if recipe not found.
    def format_recipe_results(self, uf_recipes: List[Recipe]) -> str:

        #Example output:
        #1) 01 — Torta Margherita [DOLCE] — 5 ingredienti
        #2) 05 — Frittata di Cipolle [SECONDO] — 4 ingredienti

        if not uf_recipes:
            return "Nessuna ricetta trovata."

        lines = []
        for idx, r in enumerate(uf_recipes, start=1):
            ingredient_count = len(r.ingredients)
            ingrediente_label = "ingrediente" if ingredient_count == 1 else "ingredienti"
            lines.append(f"{idx}) {r.id} — {r.title} [{r.meal_type.name}] — {ingredient_count} {ingrediente_label}")
        return "\n".join(lines)

if __name__ == "__main__":
    sl = Services()
    #meal_type = sl.get_meal_type_from_input("dolce")
    meal_type = sl.get_meal_type_from_input("secondo")

    #ingredients = sl.get_ingredient_objects(["uova", "farina", "latte"])
    ingredients = sl.get_ingredient_objects(["uova", "parmigiano", "cipolla", "olio d'oliva"])
    #ingredients = sl.get_ingredient_objects(["nutella", "farina", "latte"])
    matches = sl.find_recipes_by_meal_and_ingredients(meal_type, ingredients)
    print(sl.format_recipe_results(matches))




