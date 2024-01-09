from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('selected_restaurant', __name__)


# route for users that are not yet logged in or who have not signed up
@login_required
@views.route('/recommendation/{restaurant}', methods=['POST'])
def get_restaurant_details(restaurant_id, user_id):
    return render_template('selected_restaurant.html')



