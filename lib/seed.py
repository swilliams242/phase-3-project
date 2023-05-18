import sqlite3

DB_FILE = 'recipes.db'

# Some initial data
recipes = [
    {
        'name': 'Spaghetti Bolognese',
        'prep_time': 30,
        'instructions': 'Cook the spaghetti. Make the Bolognese sauce. Combine and serve.',
        'servings': 4,
        'image_url': 'https://www.kitchensanctuary.com/wp-content/uploads/2019/09/Spaghetti-Bolognese-square-FS-0204.jpg',
        'source_url': 'https://www.kitchensanctuary.com/spaghetti-bolognese/',
        'ingredients': ['Spaghetti', 'Tomato Sauce', 'Ground Beef', 'Onions', 'Garlic', 'Olive Oil']
    },
    {
        'name': 'Chicken Soup',
        'prep_time': 60,
        'instructions': 'Boil the chicken. Add vegetables. Simmer for one hour.',
        'servings': 6,
        'image_url': 'https://recipetineats.com/wp-content/uploads/2017/05/Chicken-Noodle-Soup-from-scratch_3.jpg',
        'source_url': 'https://www.recipetineats.com/homemade-chicken-noodle-soup-from-scratch/',
        'ingredients': ['Chicken', 'Carrots', 'Celery', 'Onions', 'Salt', 'Pepper']
    },
    # Add more recipes as needed
]

def seed_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    for recipe in recipes:
        cursor.execute(
            '''INSERT INTO recipes (name, prep_time, cooking_instructions, servings, image_url, source_url)
               VALUES (?, ?, ?, ?, ?, ?)''',
            (recipe['name'], recipe['prep_time'], recipe['instructions'], recipe['servings'], recipe['image_url'], recipe['source_url'])
        )

        recipe_id = cursor.lastrowid

        for ingredient in recipe['ingredients']:
            cursor.execute('INSERT OR IGNORE INTO ingredients (name) VALUES (?)', (ingredient,))
            cursor.execute('SELECT id FROM ingredients WHERE name = ?', (ingredient,))
            ingredient_id = cursor.fetchone()[0]
            cursor.execute('INSERT INTO recipe_ingredients (recipe_id, ingredient_id) VALUES (?, ?)', (recipe_id, ingredient_id))

    connection.commit()
    connection.close()

if __name__ == '__main__':
    seed_database()
