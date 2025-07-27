from enum import Enum

class MealType(Enum):
    ANTIPASTO = 1
    PRIMO = 2
    SECONDO = 3
    DOLCE = 4

'''future improvement: unit > 1 will be pluralized'''
'''per HW2 feedback, allows level of equivalence here 
by conceptually separating an ingredient name from the ingredient amount'''

class Ingredient:
    def __init__(self, name_italian: str, amount: str):
        self.name_italian = name_italian
        self.amount = amount

    def __repr__(self):
        return f"Ingredient(Italian='{self.name_italian}', Amount='{self.amount}')"

    def show(self):
        return f"{self.amount} di {self.name_italian}"


if __name__ == "__main__":
    meal = MealType.PRIMO
    print(meal)           # Output: Primo
    print(meal.value)     # Output: 2
    print(meal.name)      # Output: PRIMO

    ing = Ingredient("Ova", "Egg")
    print(ing)
    print(ing.__repr__())
    print(ing.get_translation())
