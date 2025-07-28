from enum import Enum
from typing import List

class MealType(Enum):
    ANTIPASTO = 1
    PRIMO = 2
    SECONDO = 3
    DOLCE = 4

'''future enhancement: amount > 1 will be pluralized'''
'''per HW2 feedback, allows level of equivalence here 
by conceptually separating an ingredient name from the ingredient amount'''

class Ingredient:
    def __init__(self, name_italian: str):
        self.name_italian = name_italian.strip().lower()

    def __eq__(self, other):
        return isinstance(other, Ingredient) and self.name_italian == other.name_italian

    def show(self):
        return f"{self.name_italian}"

class IngredientAmount:
    def __init__(self, ingredient: Ingredient, quantity: str):
        self.ingredient = ingredient
        self.quantity = quantity.strip()  # e.g., "500g", "2 cucchiai"

    def __repr__(self):
        return f"{self.quantity} di {self.ingredient.name_italian}"

class Recipe:
    def __init__(self, id : str, title: str, meal_type: MealType,
                 ingredients: List['IngredientAmount'], steps: List[str]):
        self.id = id
        self.title = title
        self.meal_type = meal_type
        self.ingredients = ingredients  # List of IngredientAmount
        self.steps = steps  # List of recipe instruction strings

    def get_ingredient_names(self) -> List[str]:
        return [ia.ingredient.name_italian for ia in self.ingredients]

    def __repr__(self):
        return f"Recipe('{self.title}', {self.meal_type}, {len(self.ingredients)} ingredients)"

    '''Enhancement: Append this recipe to a CSV file.'''
    def save_to_csv(self, filename: str):
        pass

class RecipeList:
    def __init__(self, recipes: List[Recipe] = None):
        self.recipes = recipes if recipes is not None else []

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def list_recipes(self) -> List[str]:
        """Returns a list of recipe titles prefixed with a two-digit index."""
        return [f"{i+1:02d} {r.title}" for i, r in enumerate(self.recipes)]

if __name__ == "__main__":
    pass
