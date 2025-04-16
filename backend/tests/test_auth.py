# Added so pytest treats app as a module
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_signup(client):
    res = client.post('/signup', json={
        'username': 'testuser',
        'password': 'securepass'
    })
    assert res.status_code == 201
    assert b'signup successful' in res.data 

def test_signup_existing_user(client):
    client.post('/signup', json={'username':'testuser', 'password':'pass123'})
    res = client.post('/signup', json={'username':'testuser', 'password':'pass123'})
    assert res.status_code == 409
    assert b'username already taken' in res.data

def test_login_success(client):
    client.post('/signup', json={'username': 'urmom', 'password':'pass'})
    res=client.post('/login', json={
        'username':'urmom',
        'password':'pass'
    })
    assert res.status_code == 200
    assert b'Login successful' in res.data 

def test_login_fail(client):
    res=client.post('/login', json={
        'username': 'notauser',
        'password':'wrong'
    })
    assert res.status_code == 401