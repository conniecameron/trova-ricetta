# Trova Ricetta

A simple recipe search application built with Flask and MySQL, designed to help users find Italian recipes by meal type and ingredients.

## Features

Store recipes, ingredients, and preparation steps in a MySQL database (ricetta).
Search recipes by:
    Meal type (antipasto, primo, secondo, dolce).
    Matching ingredients (default: 3).
* REST API built with Flask.
* Includes test coverage with pytest.
* Example HTML form for end-user access.

## Setup

**1. Clone Repository**
    
    git clone https://github.com/yourusername/trova-ricetta.git
    cd trova-ricetta


**2. Create and Initialize Database**

    Start MySQL and run the schema:

        mysql -u root -p < data/init.sql

    This will create a database called ricetta with tables:

   * Ingredient
   * MealType
   * Recipe
   * RecipeIngredient
   * RecipeList
   * RecipeListItem
   * RecipeStep


**3. Install Dependencies**

    python3 -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt


**4. Run the Flask App**

    app/routes.py

    The server starts at http://127.0.0.1:5000.


**5. API Usage**

    documents/documentation.md

## HTML Form Access
You can also interact via form http://127.0.0.1:5000/docs/search

web/trova_ricetta.html

