"""
ORM using SQLAlchemy for our project.  Based on the Data Model we design, will update as we learn

It seems there are multiple ways to have SQLAlchemy create the DB tables and implement the model.
1. Like CircusCircus - direct model referencing (this seems to be an older style)
2. Using DeclarativeBase - seems to be preferred way to use SQLAlchemy these days, slight changes
"""
import datetime
from flask_login import UserMixin
from . import db
from sqlalchemy import Column, Integer, String


# For user sign-up, login, session tracking, preferences, feedback tracking
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    given_name = db.Column(db.String(50), nullable=False)
    family_name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.Text)
    create_date = db.Column(db.DateTime)
    # The data below is used to capture preferences explicitly, and evals/feedback from recos
    fav_restaurant = db.Column(db.Integer)
    least_fav_restaurant = db.Column(db.Integer)
    pref_ambiance = db.Column(db.Text)
    pref_cuisine = db.Column(db.Text)
    pref_price_range =  db.Column(db.Text)
    pos_restaurants = db.Column(db.Text)
    neg_restaurants = db.Column(db.Text)
    home_city = db.Column(db.Text)
    home_state = db.Column(db.Text)

# For tracking a profile capturing user preferences, and feedback as they use the site
# class UserProfile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     fav_restaurant = db.Column(db.Integer)
#     least_fav_restaurant = db.Column(db.Integer)
#     pref_ambiance = db.Column(db.Text)
#     pref_cuisine = db.Column(db.Text)
#     pref_price_range =  db.Column(db.Text)
#     pos_restaurants = db.Column(db.Text)
#     neg_restaurants = db.Column(db.Text)
#     home_city = db.Column(db.Text)
#     home_state = db.Column(db.Text)

# For the restaurants to prefer, rate and recommend
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avg_rating = db.Column(db.Float)
    review_count = db.Column(db.Integer)
    price_range = db.Column(db.String(4))


class RestaurantRequest(db.Model):


class RestaurantReco(db.Model):


