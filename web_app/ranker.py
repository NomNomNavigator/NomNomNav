"""
This file is for the ranking algorithm
MVP:  Hard code some basic rules
"""
from . import models, db
from models import Restaurant, User



# Function to get all the data about a user needed to recommend restaurants
# In cases where user doesn't supply needed preferences in the request, fetch from profile/DB
def get_restaurant_recos(db, user):
    pass


def get_agg_rating(pos_restaurants: str):
    p_rest_list = pos_restaurants.split(',')
    r_sum, r_count = 0, 0
    for r in p_rest_list:
        r_rating = db.query(Restaurant).filterby(Restaurant.id == int(r)).first()
        r_sum = r_sum + r_rating
        r_count += 1
    agg_rating = r_sum / r_count
    avg_rating = round(agg_rating)
    return avg_rating


# Figure out if should be using a session with the DB for this function or pieces within,
# and if that needs Session = Depends()
def gather_ranking_data(user_id: int, sel_cuisine: str, ambiance: str, price_range: str, pos_restaurants: str):

    if not sel_cuisine:
        pref_cuisine = db.query(User.pref_cuisine).filterby(User.id == user_id).first()

    if not price_range:
        pref_price_range = db.query(User.pref_price_range).filterby(User.id == user_id).first()

    if not ambiance:
        pref_ambiance = db.query(User.pref_ambiance).filterby(User.id == user_id).first()

    avg_rating = get_agg_rating(pos_restaurants)





    restaurants = db.query(Restaurant)

    for restaurant in restaurants:

        avg_rating
        review_count
        price_range






