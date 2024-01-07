from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
db_name = 'database.db'


# initializing flask
def create_app():
    app = Flask(__name__)
    # secure the cookies session data; the secret key for the app
    app.config['SECRET_KEY'] = "fnocwnf4384bfgvu9wer374747230gvwsab"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # letting the database know this is the app we are going to use
    db.init_app(app)
    # importing blueprints
    from .views import views
    from .confirm import confirm
    from .models import User

    # registering the blueprints, making them accessible in the application
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(confirm)

    login_manager = LoginManager()
    login_manager.login_view = 'confirm.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(int(_id))

    return app

# def create_database(app):
#     if not path.exists('anime_web/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database~')
