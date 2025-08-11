-- Rebuild the database each time
DROP DATABASE IF EXISTS ricetta;
CREATE DATABASE ricetta CHARACTER SET utf8 COLLATE utf8_unicode_ci;;
USE ricetta;

CREATE TABLE MealType (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);
-- Create Tables
DROP TABLE IF EXISTS Ingredient;
CREATE TABLE Ingredient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_italian VARCHAR(100) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS Recipe;
CREATE TABLE Recipe (
    id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    meal_type ENUM('ANTIPASTO','PRIMO','SECONDO','DOLCE') NOT NULL
);

DROP TABLE IF EXISTS RecipeIngredient;
CREATE TABLE RecipeIngredient (
    recipe_id VARCHAR(10) NOT NULL,
    ingredient_id INT NOT NULL,
    quantity VARCHAR(50) NOT NULL,
    PRIMARY KEY (recipe_id, ingredient_id),
    CONSTRAINT fk_ri_recipe FOREIGN KEY (recipe_id) REFERENCES Recipe(id) ON DELETE CASCADE,
    CONSTRAINT fk_ri_ingredient FOREIGN KEY (ingredient_id) REFERENCES Ingredient(id) ON DELETE RESTRICT
);

DROP TABLE IF EXISTS RecipeStep;
CREATE TABLE RecipeStep (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id VARCHAR(10) NOT NULL,
    step_number INT NOT NULL,
    text TEXT NOT NULL,
    verbs JSON NULL,
    CONSTRAINT uq_step UNIQUE (recipe_id, step_number),
    CONSTRAINT fk_step_recipe FOREIGN KEY (recipe_id) REFERENCES Recipe(id) ON DELETE CASCADE,
    CHECK (JSON_VALID(verbs) OR verbs IS NULL)
);

DROP TABLE IF EXISTS RecipeList;
CREATE TABLE RecipeList (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS RecipeListItem;
CREATE TABLE RecipeListItem (
    recipe_list_id INT NOT NULL,
    recipe_id VARCHAR(10) NOT NULL,
    position INT NOT NULL,
    PRIMARY KEY (recipe_list_id, recipe_id),
    CONSTRAINT fk_rli_list FOREIGN KEY (recipe_list_id) REFERENCES RecipeList(id) ON DELETE CASCADE,
    CONSTRAINT fk_rli_recipe FOREIGN KEY (recipe_id) REFERENCES Recipe(id) ON DELETE CASCADE
);

-- Populate Tables with sample data'''
-- 5 recipes with 3-5 unique ingredients each'''

-- Ingredients
INSERT INTO Ingredient (name_italian) VALUES
('farina'),
('zucchero'),
('uova'),
('burro'),
('latte'),
('pomodori'),
('mozzarella'),
('basilico'),
('pasta'),
('aglio'),
('olio d''oliva'),
('cipolla'),
('carne macinata'),
('parmigiano');

-- Recipes
INSERT INTO Recipe (id, title, meal_type) VALUES
('01', 'Torta Margherita', 'DOLCE'),
('02', 'Pasta al Pomodoro', 'PRIMO'),
('03', 'Insalata Caprese', 'ANTIPASTO'),
('04', 'Ragù alla Bolognese', 'SECONDO'),
('05', 'Frittata di Cipolle', 'SECONDO');

-- Map ingredient names to IDs
-- Torta Margherita
INSERT INTO RecipeIngredient (recipe_id, ingredient_id, quantity) VALUES
('01', (SELECT id FROM Ingredient WHERE name_italian='farina'), '200g'),
('01', (SELECT id FROM Ingredient WHERE name_italian='zucchero'), '150g'),
('01', (SELECT id FROM Ingredient WHERE name_italian='uova'), '3'),
('01', (SELECT id FROM Ingredient WHERE name_italian='burro'), '100g'),
('01', (SELECT id FROM Ingredient WHERE name_italian='latte'), '100ml');

-- Pasta al Pomodoro
INSERT INTO RecipeIngredient (recipe_id, ingredient_id, quantity) VALUES
('02', (SELECT id FROM Ingredient WHERE name_italian='pasta'), '200g'),
('02', (SELECT id FROM Ingredient WHERE name_italian='pomodori'), '3'),
('02', (SELECT id FROM Ingredient WHERE name_italian='aglio'), '1 spicchio'),
('02', (SELECT id FROM Ingredient WHERE name_italian='olio d''oliva'), '2 cucchiai'),
('02', (SELECT id FROM Ingredient WHERE name_italian='basilico'), 'qualche foglia');

-- Insalata Caprese
INSERT INTO RecipeIngredient (recipe_id, ingredient_id, quantity) VALUES
('03', (SELECT id FROM Ingredient WHERE name_italian='mozzarella'), '150g'),
('03', (SELECT id FROM Ingredient WHERE name_italian='pomodori'), '2'),
('03', (SELECT id FROM Ingredient WHERE name_italian='basilico'), 'qualche foglia'),
('03', (SELECT id FROM Ingredient WHERE name_italian='olio d''oliva'), '1 cucchiaio');

-- Ragù alla Bolognese
INSERT INTO RecipeIngredient (recipe_id, ingredient_id, quantity) VALUES
('04', (SELECT id FROM Ingredient WHERE name_italian='carne macinata'), '250g'),
('04', (SELECT id FROM Ingredient WHERE name_italian='cipolla'), '1'),
('04', (SELECT id FROM Ingredient WHERE name_italian='olio d''oliva'), '2 cucchiai'),
('04', (SELECT id FROM Ingredient WHERE name_italian='pomodori'), '2'),
('04', (SELECT id FROM Ingredient WHERE name_italian='parmigiano'), '50g');

-- Frittata di Cipolle
INSERT INTO RecipeIngredient (recipe_id, ingredient_id, quantity) VALUES
('05', (SELECT id FROM Ingredient WHERE name_italian='uova'), '4'),
('05', (SELECT id FROM Ingredient WHERE name_italian='cipolla'), '1 grande'),
('05', (SELECT id FROM Ingredient WHERE name_italian='olio d''oliva'), '2 cucchiai'),
('05', (SELECT id FROM Ingredient WHERE name_italian='parmigiano'), '30g');

-- This is NOT fully working yet; json format issues

-- Recipe steps (verbs stored as JSON arrays; keep null if not extracted yet)
INSERT INTO RecipeStep (recipe_id, step_number, text, verbs) VALUES
('01', 1, 'Mescola farina, zucchero e uova.', JSON_ARRAY('mescolare')),
('01', 2, 'Aggiungi burro fuso e latte.', JSON_ARRAY('aggiungere')),
('01', 3, 'Inforna a 180°C per 35 minuti.', JSON_ARRAY('infornare')),

('02', 1, 'Cuoci la pasta in acqua salata.', JSON_ARRAY('cuocere')),
('02', 2, 'Prepara il sugo con pomodori, aglio e olio.', JSON_ARRAY('preparare')),
('02', 3, 'Mescola la pasta con il sugo e guarnisci con basilico.', JSON_ARRAY('mescolare','guarnire')),

('03', 1, 'Affetta la mozzarella e i pomodori.', JSON_ARRAY('affettare')),
('03', 2, 'Disponi su un piatto alternando le fette.', JSON_ARRAY('disporre','alternare')),
('03', 3, 'Condisci con olio e basilico.', JSON_ARRAY('condire')),

('04', 1, 'Soffriggi la cipolla nell\'olio.', JSON_ARRAY('soffriggere')),
('04', 2, 'Aggiungi la carne e rosola bene.', JSON_ARRAY('aggiungere','rosolare')),
('04', 3, 'Unisci i pomodori e cuoci a fuoco lento.', JSON_ARRAY('unire','cuocere')),
('04', 4, 'Servi con parmigiano grattugiato.', JSON_ARRAY('servire')),

('05', 1, 'Affetta e soffriggi la cipolla.', JSON_ARRAY('affettare','soffriggere')),
('05', 2, 'Sbatti le uova con parmigiano.', JSON_ARRAY('sbattere')),
('05', 3, 'Cuoci in padella fino a doratura.', JSON_ARRAY('cuocere'));

-- Sample recipe list and its items
-- Recipe list and ordered membership (no window functions)
INSERT INTO RecipeList (name) VALUES ('Ricette Facili');
SET @pos := 0;
INSERT INTO RecipeListItem (recipe_list_id, recipe_id, position)
SELECT rl.id, r.id, (@pos := @pos + 1) AS position
FROM RecipeList rl
JOIN Recipe r
  ON 1=1
WHERE rl.name = 'Ricette Facili'
ORDER BY r.id;
