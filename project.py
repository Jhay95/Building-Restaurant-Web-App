from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Base, Restaurant, MenuItem

# Initiate app
app = Flask(__name__)

# Connect to Database engine
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
session = scoped_session(sessionmaker(bind=engine))

@app.teardown_request
def remove_session(ex=None):
    session.remove()

# List all restaurants in the database
@app.route('/')
@app.route('/restaurants/')
def restaurantList():  
    restaurants = session.query(Restaurant)
    return render_template('restaurants.html', restaurants=restaurants)


# List all menus of a selected Restaurant
@app.route('/restaurants/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant, items=items, restaurant_id=restaurant_id)


# Edit a menu item
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return render_template('editmenu.html', restaurant_id=restaurant_id, menu_id=menu_id, item=item)


# Delete a menu Item from a Restaurant's Menu list
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    return


# Add a new menu item to a Restaurant




# Add a new Restaurant 




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
