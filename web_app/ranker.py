"""
This file is for the ranking algorithm
MVP:  Hard code some basic rules
"""
from . import models, db
from models import Restaurant, User
from sqlalchemy import select


# Function to get all the data about a user needed to recommend restaurants
# In cases where user doesn't supply needed preferences in the request, fetch from profile/DB
def get_restaurant_recos(db, user):
    pass


# Function to figure out from user liked restaurants what their preferred price range might be.
# We could instead ask them to enter a preferred price range in their profile -> need to add column to model/migrate
def get_agg_rating(pos_restaurants: str) -> float:
    p_rest_list = pos_restaurants.split(',')
    r_sum, r_count = 0, 0
    for r in p_rest_list:
        r_rating = db.session.execute(select(Restaurant.avg_rating).where(Restaurant.id == int(r)))
        r_sum = r_sum + r_rating
        r_count += 1
    agg_rating = r_sum / r_count
    avg_rating = round(agg_rating)
    return avg_rating


# Figure out if should be using a session with the DB for this function or pieces within,
# and if that needs Session = Depends()
def gather_ranking_data(user_id: int, cuisine: str, ambiance: str, price_range: str, pos_restaurants: str):

    if not cuisine:
        cuisine = db.session.execute(select(User.pref_cuisine).where(User.id == user_id))

    if not price_range:
        price_range = db.session.execute(select(User.pref_price_range).where(User.id == user_id))

    if not ambiance:
        ambiance = db.session.execute(select(User.pref_ambiance).where(User.id == user_id))

    avg_rating = get_agg_rating(pos_restaurants)

    # Search:  Restaurants with a matching cuisine, exact matching price range, avg_rating within .5
    search_match_restaurants = db.session.execute(
    # Sort/Rank: If ambiance exists, rank match first.
    # Sort/Rank: Avg_rating high to low.
