# Added so pytest treats app as a module
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app, db 

@pytest.fixture 
def app():
    app = create_app()
    app.config['TESTING'] = True 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory'
    app.config['SECRET_KEY'] = 'test_secret'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture 
def client(app):
    return app.test_client()