# this is where you run your program

import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Recipe Name', help='Name of the recipe')
@click.option('--prep-time', type=int, prompt='Preparation Time', help='Preparation time in minutes')
@click.option('--instructions', prompt='Cooking Instructions', help='Cooking instructions')
@click.option('--servings', type=int, prompt='Servings', help='Number of servings')
@click.option('--image-url', prompt='Image URL', help='URL of the recipe image')
@click.option('--source-url', prompt='Source URL', help='URL of the recipe source')
def add_recipe(name, prep_time, instructions, servings, image_url, source_url):
    # Logic to add the recipe to the database
    click.echo('Recipe added successfully.')

@cli.command()
@click.argument('recipe_id', type=int)
def delete_recipe(recipe_id):
    # Logic to delete the recipe from the database
    click.echo(f'Recipe {recipe_id} deleted successfully.')

@cli.command()
def search_recipes():
    # Logic to search and display recipes based on certain criteria
    click.echo('Displaying search results.')

if __name__ == '__main__':
    cli()
