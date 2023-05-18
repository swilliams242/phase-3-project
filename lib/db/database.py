import sqlite3

connection = sqlite3.connect('../recipes.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      prep_time INTEGER,
                      cooking_instructions TEXT,
                      servings INTEGER,
                      image_url TEXT,
                      source_url TEXT
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                      id INTEGER PRIMARY KEY,
                      name TEXT UNIQUE
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS recipe_ingredients (
                      recipe_id INTEGER,
                      ingredient_id INTEGER,
                      FOREIGN KEY(recipe_id) REFERENCES recipes(id),
                      FOREIGN KEY(ingredient_id) REFERENCES ingredients(id),
                      PRIMARY KEY (recipe_id, ingredient_id)
               )''')

connection.commit()
connection.close()
