from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)


# route for users that are not yet logged in or who have not signed up
@views.route('/')
def access():
    return render_template('index.html')


# home page of the users that are logged in
@views.route('/home')
# @login_required
def home():
    return render_template('home.html')
