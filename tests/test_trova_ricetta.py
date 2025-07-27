from app.trova_ricetta import *
'''import pytest'''

def test_meal_type():
    meal_type = MealType(4)
    assert meal_type == meal_type.DOLCE
    assert meal_type.value == 4
    assert meal_type.name == "DOLCE"

def test_ingredient():
    ingredient = Ingredient("ova", "3")
    assert ingredient.show() == "3 di ova"







