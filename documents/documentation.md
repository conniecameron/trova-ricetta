### **Base URL**

http://127.0.0.1:5000

### **Endpoints**

#### **GET /health**

API health check

##### **Response 200**

{"status":"ok"}

#### **GET /recipes/all**

Returns all recipes from the database (id, title, meal_type, ingredients, steps).

##### **Response 200**

{
  "recipes": [
    {
      "id": "01",
      "title": "Torta Margherita",
      "meal_type": "DOLCE",
      "ingredients": ["farina","zucchero","uova","burro","latte"],
      "steps": ["Mescola...", "Aggiungi...", "Inforna..."]
    },
    ...
  ]
}

#### POST /recipes/search

Search for recipes by meal type and ingredients. The service:

* validates meal_type (ANTIPASTO | PRIMO | SECONDO | DOLCE),
* converts the provided ingredient checklist into objects,
* returns recipes of that meal type with at least 3 overlapping ingredients

##### **Request body (JSON)**

{
  "meal_type": "dolce",
  "ingredients": ["uova", "farina", "latte"],
  "min_matches": 3
}

##### **Successful Response 200**

{
  "recipes": [
    {
      "id": "01",
      "title": "Torta Margherita",
      "meal_type": "DOLCE",
      "match_count": 3,
      "ingredients": ["farina","zucchero","uova","burro","latte"],
      "steps": ["Mescola farina, zucchero e uova.","Aggiungi burro fuso e latte.","Inforna a 180°C per 35 minuti."]
    }
  ]
}

##### **Error Response 404 Not Found**

{"error":{"code":404,"message":"Nessuna ricetta trovata."}}

### Accessing the API directly
**cURL**

#### Health
curl -s http://127.0.0.1:5000/health

#### All recipes
curl -s http://127.0.0.1:5000/recipes/all | jq

#### Search (≥3 ingredient matches)
curl -s -X POST http://127.0.0.1:5000/recipes/search \
  -H "Content-Type: application/json" \
  -d '{"meal_type":"dolce","ingredients":["uova","farina","latte"],"min_matches":3}' | jq

### Accessing the API via HTML form

http://127.0.0.1:5000/docs/search

1) Select a meal type from the **Meal Type** dropdown
2) Select ingredients from the **Ingredients** checklist
3) Click the **Trova Ricetta** button to search for a matching recipe.