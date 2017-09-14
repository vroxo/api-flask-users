import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__) # Flask app

    app_settings = os.getenv('APP_SETTINGS') # Get app settings
    app.config.from_object(app_settings) # Apply settings

    db.init_app(app) # init DB

    from core.api.views import users_blueprint
    app.register_blueprint(users_blueprint) # Register blueprint

    return app # retuen my app
