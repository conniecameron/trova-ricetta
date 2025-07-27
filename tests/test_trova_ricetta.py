from app.trova_ricetta import *
'''import pytest'''

def test_meal_type():
    meal_type = MealType(4)
    assert meal_type == meal_type.DOLCE
    assert meal_type.value == 4
    assert meal_type.name == "DOLCE"

def test_ingredient():
    ingredient = Ingredient("ova")
    assert ingredient.show() == "ova"

def test_ingredient_amount():
    ingredient = Ingredient("farina")
    item1 = IngredientAmount(ingredient, "500g") #500g of flour
    item2 = IngredientAmount(Ingredient("FARINA"), "2 cucchiai") #2 spoons of flour

    '''per HW2 feedback, checks lexical equivalence accdg to ingredient name'''

    assert item1.__repr__() == "500g di farina"
    assert item2.__repr__() == "2 cucchiai di farina"
    assert item1.ingredient == item2.ingredient

    if (item1.ingredient == item2.ingredient):
        print(f"\n{item1} and {item2} are the same")
    else:
        print(f"\n{item1} and {item2} are not the same")






