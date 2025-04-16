from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_session import Session
import os

db = SQLAlchemy()

def create_app(test_config = None):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Switch to pytest config if available
    if test_config:
        app.config.update(test_config)

    # Configure CORS with proper settings for credentials
    CORS(
        app,
        supports_credentials=True,
        origins="*",
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
        expose_headers=["Content-Type", "Authorization"],
        max_age=3600
    )
    app.config["SESSION_TYPE"] = "filesystem" # TODO: switch to redis for prod
    app.config["SESSION_PERMANENT"] = False   

    Session(app) 

    db.init_app(app)

    with app.app_context():
        from .routes.auth_routes import auth_bp
        from .routes.dashboard_routes import dashboard_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(dashboard_bp)

        db.create_all()
    print("DATABASE URI:", app.config["SQLALCHEMY_DATABASE_URI"])

    return app
