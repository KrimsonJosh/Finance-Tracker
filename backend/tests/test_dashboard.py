# Added so pytest treats app as a module
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db 

def signup_and_login(client):
    client.post('/signup', json = {"username": "dashboarduser", "password": "pass"})
    return client

def test_expense_post_and_get(client):
    client = signup_and_login(client) 

    # POST Expense
    res = client.post('/api/expenses', json={
        "amount":100,
        "category": "Cookies"
    })
    assert res.status_code == 201 

    # GET Expense
    res = client.get('/api/expenses')
    assert res.status_code == 200
    data = res.get_json() 
    assert data["success"] is True 
    assert len(data["expenses"]) == 1
    assert data["expenses"][0]["category"] == "Cookies" 
    assert data["expenses"][0]["amount"] == 100 

def test_expense_put_and_delete(client):
    client = signup_and_login(client) 
    # add expense
    client.post('/api/expenses', json={
        "amount": 20,
        "category": "Food"
    })
    res = client.get('/api/expenses')
    expense_id = res.get_json()["expenses"][0]["id"]

    #PUT route
    res = client.put(f'/api/expenses/{expense_id}', json={
        "amount":200,
        "category": "Housing"
    })
    assert res.status_code == 200
    assert b'expense updated successfully' in res.data

    # delete route 
    res = client.delete(f'/api/expenses/{expense_id}')
    assert res.status_code == 200
    assert b'deleted successfully' in res.data

    # check that its gone
    res = client.get('/api/expenses') 
    assert res.status_code == 200
    assert res.get_json()["expenses"] == [] 

def test_expense_without_auth(client):
    res = client.get('/api/expenses')
    assert res.status_code == 401

    res = client.post('/api/expenses', json={
        'amount': 200,
        'category': 'bru u'
    })
    assert res.status_code == 401 

def test_income_flow(client):
    client = signup_and_login(client) 

    res = client.get('/api/income')
    assert res.status_code == 404

    from app.models import Income, User 
    user = User.query.filter_by(username="dashboarduser").first() 
    income = Income(user_id=user.id, amount=1000)
    db.session.add(income)
    db.session.commit()

    # GET Income
    res = client.get('/api/income')
    assert res.status_code == 200
    assert res.get_json()["income"] == 1000

    # PUT income
    res = client.put('/api/income', data={"amount": 1500})
    assert res.status_code == 200
    assert b'income updated successfully' in res.data 

    #confirm new income 
    res = client.get('/api/income') 
    assert res.get_json()['income'] == 1500 

def test_income_auth_reqiured(client):
    res = client.get('/api/income')
    assert res.status_code == 401 

    res=client.put('/api/income', data={'amount': 3000})
    assert res.status_code == 401