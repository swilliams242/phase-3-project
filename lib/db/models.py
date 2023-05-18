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

connection.commit()
connection.close()
