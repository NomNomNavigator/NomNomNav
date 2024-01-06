from flask import Blueprint, render_template

# initializing blueprint
confirm = Blueprint('confirm', __name__)


@confirm.route('/login', methods=['POST', "GET"])
def login():
    return render_template('login.html')
