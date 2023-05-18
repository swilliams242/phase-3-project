import click
import sqlite3

DB_FILE = '../recipes.db'

@click.group()
def cli():
    pass


#functionality to add a recipe
@cli.command()
@click.option('--name', prompt='Recipe Name', help='Name of the recipe')
@click.option('--prep-time', type=int, prompt='Preparation Time', help='Preparation time in minutes')
@click.option('--instructions', prompt='Cooking Instructions', help='Cooking instructions')
@click.option('--servings', type=int, prompt='Servings', help='Number of servings')
@click.option('--image-url', prompt='Image URL', help='URL of the recipe image')
@click.option('--source-url', prompt='Source URL', help='URL of the recipe source')
@click.option('--ingredients', prompt='Ingredients', help='Ingredients of the recipe', multiple=True)
def add_recipe(name, prep_time, instructions, servings, image_url, source_url, ingredients):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO recipes (name, prep_time, cooking_instructions, servings, image_url, source_url)
                      VALUES (?, ?, ?, ?, ?, ?)''', (name, prep_time, instructions, servings, image_url, source_url))

    recipe_id = cursor.lastrowid

    for ingredient in ingredients:
        cursor.execute('INSERT OR IGNORE INTO ingredients (name) VALUES (?)', (ingredient,))
        cursor.execute('SELECT id FROM ingredients WHERE name = ?', (ingredient,))
        ingredient_id = cursor.fetchone()[0]
        cursor.execute('INSERT INTO recipe_ingredients (recipe_id, ingredient_id) VALUES (?, ?)', (recipe_id, ingredient_id))
        
    connection.commit()
    connection.close()

    click.echo('Recipe added successfully.')


#updating a recipe
@cli.command()
@click.option('--recipe_id', type=int, prompt='Recipe ID', help='ID of the recipe you want to update')
@click.option('--name', prompt='Recipe Name', help='Name of the recipe')
@click.option('--prep-time', type=int, prompt='Preparation Time', help='Preparation time in minutes')
@click.option('--instructions', prompt='Cooking Instructions', help='Cooking instructions')
@click.option('--servings', type=int, prompt='Servings', help='Number of servings')
@click.option('--image-url', prompt='Image URL', help='URL of the recipe image')
@click.option('--source-url', prompt='Source URL', help='URL of the recipe source')
def update_recipe(recipe_id, name, prep_time, instructions, servings, image_url, source_url):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute('''UPDATE recipes
                      SET name = ?, prep_time = ?, cooking_instructions = ?, servings = ?, image_url = ?, source_url = ?
                      WHERE id = ?''',
                   (name, prep_time, instructions, servings, image_url, source_url, recipe_id))

    if cursor.rowcount == 1:
        connection.commit()
        click.echo(f'Recipe {recipe_id} updated successfully.')
    else:
        click.echo(f'Recipe {recipe_id} not found.')

    connection.close()


#deleting a recipe
@cli.command()
@click.argument('recipe_id', type=int)
def delete_recipe(recipe_id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
    
    if cursor.rowcount == 1:
        connection.commit()
        click.echo(f'Recipe {recipe_id} deleted successfully.')
    else:
        click.echo(f'Recipe {recipe_id} not found.')
    
    connection.close()


#searching for a recipe
@cli.command()
@click.option('--name', default=None, help='Filter recipes by name (case insensitive, partial match allowed)')
def search_recipes(name):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    if name:
        query = f'SELECT * FROM recipes WHERE name LIKE ?'
        cursor.execute(query, (f'%{name}%',))
    else:
        query = 'SELECT * FROM recipes'
        cursor.execute(query)

    recipes = cursor.fetchall()

    for recipe in recipes:
        click.echo(f'Recipe ID: {recipe[0]}, Name: {recipe[1]}')
        click.echo(f'Preparation Time: {recipe[2]} minutes')
        click.echo(f'Cooking Instructions: {recipe[3]}')
        click.echo(f'Servings: {recipe[4]}')
        click.echo(f'Image URL: {recipe[5]}')
        click.echo(f'Source URL: {recipe[6]}')
        click.echo('---------------------------')

    connection.close()


if __name__ == '__main__':
    cli()
