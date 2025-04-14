from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials = True)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .routes.auth_routes import auth_bp
        from .routes.dashboard_routes import dashboard_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(dashboard_bp)

        db.create_all()

    return app
