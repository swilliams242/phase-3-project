from . import CONN, CURSOR

class Ingredients () :
    
    def __init__(self, name, section, quantity, id = None) :
        self.name = name
        self.section = section
        self.quantity = quantity
        self.id = id

    @property
    def name(self) :
        return self._name
    
    @name.setter
    def name(self, name) :
        if type(name) is str and name :
            self._name = name
        else : raise Exception('Ingredient name must be a string and greater than zero characters.')

    @property
    def section(self) :
        return self._section
    
    @section.setter
    def section(self, section) :
        if type(section) is str and section :
            self._section = section
        else : raise Exception('Ingredient section must be a string and greater than zero characters.')

    @property
    def quantity(self) :
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity) :
        if type(quantity) is int and quantity :
            self._quantity = quantity
        else : raise Exception('Ingredient quantity must be a number and greater than zero characters.')

    @classmethod
    def create_table(cls) :
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY,
                name TEXT,
                section TEXT,
                quantity INTEGER
            )
        """)
        print('Table was created.')

    @classmethod
    def create (cls, name, section, quantity) :
        ingredient = Ingredients(name, section, quantity)
        CURSOR.execute(f"""
            INSERT INTO ingredient (name, section, quantity)
            VALUE ('{ingredient.name}', '{ingredient.section}', '{ingredient.quantity}')
        """)

    @classmethod
    def all(cls) :
        sql = "SELECT * from ingredients" 

        ingredients = CURSOR.execute(sql).fetchall()
        return [cls.db_into_instance(ingredient) for ingredient in ingredients]
    
    @classmethod
    def db_into_instance (cls, ingredient) :
        return Ingredients(ingredient[1], ingredient[2], ingredient[3], ingredient[0])
    
