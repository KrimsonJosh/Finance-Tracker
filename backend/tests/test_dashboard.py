import pytest
from app import create_app, db 
from app.models import User, Expense

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True