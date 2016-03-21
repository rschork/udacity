import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    __table_args__ = (UniqueConstraint('id', name='id_1'),UniqueConstraint('name', name='name_1'))

    UniqueConstraint('name', name='name_1')

class CategoryItem(Base):
    __tablename__ = 'category_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    ts_created = Column(DateTime, default=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
    ts_updated = Column(DateTime, onupdate=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
    category = relationship(Category)

    UniqueConstraint('name', name='name_1')

if __name__ == '__main__':
    engine = create_engine('sqlite:///itemcatalog.db')
    Base.metadata.create_all(engine)
