from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# route for users that are not yet logged in or who have not signed up
@views.route('/')
def access():
    return render_template('base.html')


# home page of the users that are logged in
@views.route('/home')
def home():
    return render_template('home.html')
