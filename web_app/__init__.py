from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


# initializing flask
def create_app():
    app = Flask(__name__)
    # secure the cookies session data; the secret key for the app
    app.config['SECRET_KEY'] = "fnocwnf4384bfgvu9wer374747230gvwsab"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # letting the database know this is the app we are going to use
    db.init_app(app)
    # importing blueprints
    from .views import views
    from .confirm import confirm

    # registering the blueprints, making them accessible in the application
    app.register_blueprint(views)
    app.register_blueprint(confirm)
