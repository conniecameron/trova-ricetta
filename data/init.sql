CREATE DATABASE IF NOT EXISTS ricetta;
USE ricetta;

CREATE TABLE MealType (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO MealType (id, name)
VALUES
    (1, 'ANTIPASTO'),
    (2, 'PRIMO'),
    (3, 'SECONDO'),
    (4, 'DOLCE');

CREATE TABLE Ingredient (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO Ingredient (id, name)
VALUES
    (1, 'farina'),
    (2, 'zucchero'),
    (3, 'uova'),
    (4, 'burro'),
    (5, 'latte'),
    (6, 'pomodori'),
    (7, 'mozzarella'),
    (8, 'basilico'),
    (9, 'pasta'),
    (10, 'aglio'),
    (11, 'olio d''oliva'),
    (12, 'cipolla'),
    (13, 'carne macinata'),
    (14, 'parmigiano');

CREATE TABLE Recipe (
    id VARCHAR(5) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    meal_type_id INT,
    FOREIGN KEY (meal_type_id) REFERENCES MealType(id)
);

INSERT INTO Recipe (id, title, meal_type_id)
VALUES
    ('01', 'Torta Margherita', 4),
    ('02', 'Pasta al Pomodoro', 2),
    ('03', 'Insalata Caprese', 1),
    ('04', 'Ragù alla Bolognese', 3),
    ('05', 'Frittata di Cipolle', 3);


