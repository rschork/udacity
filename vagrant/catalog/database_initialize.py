import os
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def add_cat(sport_name, session):
    sport = Category(name = sport_name)
    session.add(sport)

def add_item(sport_name, sport_item, desc, session):
    sport_query = session.query(Category).filter_by(name = sport_name)
    sport_item = CategoryItem(name = sport_item, description = desc, category_id = sport_query[0].id)
    session.add(sport_item)

for sport in ["Basketball", "Soccer", "Futsal", "Baseball", "Lacrosse"]:
    add_cat(sport,session)

add_item("Basketball", "Wilson Basketball", "Wilson Official NBA Basketball", session)
add_item("Basketball", "Nike Air Jordan", "Nike Air Jordan Shoes", session)
add_item("Basketball", "Price Throwback Jersey", "Mark Price Cavs Throwback Jersey", session)
add_item("Futsal", "Match Futsal Ball", "Officially Sanctioned FIFA Futsal Matchball", session)
add_item("Soccer", "Adidas Copa Mundial", "Adidas Copa Mundial Kangaroo Leather Cleats", session)
add_item("Soccer", "Nike GK Vapor", "Nike Vapor Grip Goalkeeper Gloves", session)
add_item("Lacrosse", "Warrior Revolution Head", "Warrior Revolution Lacrosse Stick Head", session)
add_item("Baseball", "Wilson Baseball Glove", "Wilson Leather Baseball Glove - Right Handed", session)

session.commit()
print session.query(Category).all()
