import sqlite3

CONN = sqlite3.connect('recipe_database.db')
CURSOR = CONN.cursor()

