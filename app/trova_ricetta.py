from enum import Enum

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

    def __hash__(self):
        return hash(self.name_italian)

    def show(self):
        return f"{self.name_italian}"

class IngredientAmount:
    def __init__(self, ingredient: Ingredient, quantity: str):
        self.ingredient = ingredient
        self.quantity = quantity.strip()  # e.g., "500g", "2 cucchiai"

    def __repr__(self):
        return f"{self.quantity} di {self.ingredient.name_italian}"

if __name__ == "__main__":
    pass
