from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_session import Session

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configure CORS with proper settings for credentials
    CORS(
        app,
        supports_credentials=True,
        origins=["http://localhost:5173", "http://127.0.0.1:5173"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
        expose_headers=["Content-Type", "Authorization"],
        max_age=3600
    )
    app.config["SESSION_TYPE"] = "filesystem" # TODO: switch to redis for prod
    app.config["SESSION_PERMANENT"] = False  
    app.config["SESSION_USE_SIGNER"] = True    

    Session(app) 

    db.init_app(app)

    with app.app_context():
        from .routes.auth_routes import auth_bp
        from .routes.dashboard_routes import dashboard_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(dashboard_bp)

        db.create_all()

    return app
