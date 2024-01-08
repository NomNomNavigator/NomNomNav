"""
This file is for the ranking algorithm
MVP:  Hard code some basic rules
"""
from . import models, db

# Function to get all the data about a user needed to recommend restaurants
# In cases where user doesn't supply needed preferences in the request, fetch from profile/DB
def gather_ranking_data(db, user):




def get_restaurant_recos():
    user_info = gather_ranking_data(db, user)
    
