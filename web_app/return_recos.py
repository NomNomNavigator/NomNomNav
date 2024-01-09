from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)


# route for users that are not yet logged in or who have not signed up
@login_required
@views.route('/recommendations', methods=['POST'])
def get_recos():
    return render_template('index.html')



