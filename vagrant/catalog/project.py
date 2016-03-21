from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/itemcatalog')
def itemCatalog():
    categories = session.query(Category).all()
    return render_template('template.html', categories=categories)

@app.route('/itemcatalog/<string:category_name>')
def specificCategory(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(CategoryItem).filter_by(category_id = category.id)
    return render_template('item_template.html', category=category, items=items)

@app.route('/itemcatalog/<int:category_id_int>')
def specificCategoryInt(category_id_int):
    category = session.query(Category).filter_by(id=category_id_int).one()
    return redirect(url_for('specificCategory', category_name=category.name))

@app.route('/itemcatalog/<string:category_name>/new', methods=['GET','POST'])
def newCategoryItem(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(CategoryItem).filter_by(category_id = category.id)
    if request.method == 'POST':
        newItem = CategoryItem(name = request.form['name'], description = request.form['description'], category_id = category.id)
        session.add(newItem)
        session.commit()
        flash("new item created!")
        return redirect(url_for('specificCategory', category_name=category_name))
    else:
        return render_template('newCategoryItem.html', category=category, items=items)

@app.route('/itemcatalog/<string:category_name>/<int:item_id>/edit', methods=['GET','POST'])
def editCategoryItem(category_name, item_id):
    category = session.query(Category).filter_by(name=category_name).one()
    editedItem = session.query(CategoryItem).filter_by(category_id=category.id, id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('specificCategory', category_name=category.name))
    else:
        return render_template('editCategoryItem.html', category_name=category.name, item=editedItem)

@app.route('/itemcatalog/<string:category_name>/<int:item_id>/delete', methods=['GET','POST'])
def deleteCategoryItem(category_name, item_id):
    category = session.query(Category).filter_by(name=category_name).one()
    editedItem = session.query(CategoryItem).filter_by(category_id=category.id, id=item_id).one()
    if request.method == 'POST':
        session.delete(editedItem)
        session.commit()
        return redirect(url_for('specificCategory', category_name=category.name))
    else:
        return render_template('deleteCategoryItem.html', category_name=category.name, item=editedItem)


if __name__ == '__main__':
    app.secret_key = 'SuperSecretKey'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
