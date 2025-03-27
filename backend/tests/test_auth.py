import pytest 
from app import create_app
from app.models import User  

@pytest.fixture 
def client():
    app = create_app()
    user = User() 
