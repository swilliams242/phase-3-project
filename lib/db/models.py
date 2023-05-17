from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    prep_time = Column(Integer)
    cooking_instructions = Column(String)
    servings = Column(Integer)
    image_url = Column(String)
    source_url = Column(String)
