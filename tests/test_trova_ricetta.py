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

'''Create a recipe for Torta Facile and save to a csv file'''
def test_recipe():

    #Define some ingredients
    egg = Ingredient("uova")
    flour = Ingredient("farina")
    milk = Ingredient("latte")
    sugar = Ingredient("zucchero")

    #Define ingredient amounts
    ingredients = [
        IngredientAmount(egg, "2"),
        IngredientAmount(flour, "200g"),
        IngredientAmount(milk, "100ml"),
        IngredientAmount(sugar, "50g")
    ]

    #Define steps for the recipe
    steps = [
        "Sbatti le uova con lo zucchero.",
        "Aggiungi la farina e mescola bene.",
        "Versa il latte lentamente e continua a mescolare.",
        "Cuoci in forno a 180°C per 30 minuti."
    ]

    #Create the recipe
    torta = Recipe("01", title="Torta Facile", meal_type=MealType.DOLCE, ingredients=ingredients, steps=steps)

    #Display ingredient names
    assert torta.get_ingredient_names() == ['uova', 'farina', 'latte', 'zucchero']
    print("\nIngredienti richiesti:", torta.get_ingredient_names())

def test_recipe_list():
    recipe1 = (Recipe("01", "Torta Facile", meal_type=MealType.DOLCE, ingredients = [], steps = []))
    recipe2 = (Recipe("02", "Torta Firenze", meal_type=MealType.DOLCE, ingredients = [], steps = []))
    recipe3 = (Recipe("03", "Torta della Nonna", meal_type=MealType.DOLCE, ingredients = [], steps = []))

    recipe_list = RecipeList()
    recipe_list.add_recipe(recipe1)
    recipe_list.add_recipe(recipe2)
    recipe_list.add_recipe(recipe3)

    result = recipe_list.list_recipes()
    assert result == ["01 Torta Facile", "02 Torta Firenze", "03 Torta della Nonna"]
    assert len(result) == 3
    recipe_list.add_recipe((Recipe("04", "Torta della Casa", meal_type=MealType.DOLCE, ingredients = [], steps = [])))
    result = recipe_list.list_recipes()
    assert len(result) == 4

    for rec in result: print(rec)






