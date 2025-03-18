from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
from ..models import db, Expense, Income

dashboard_bp = Blueprint('dashboard', __name__)
'''
------------
ROUTE: ADD EXPENSE
-----------
'''
@dashboard_bp.route('/api/expenses', methods = ['POST'])
def addExpense():

    user_id = session.get('user_id') 
    if not user_id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    amount = request.form.get('amount')
    category = request.form.get('category')
    if not amount or not category:
        return jsonify({'success': False, 'message': "Amount and category required"}), 400
    
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'success': False, 'message': 'Amount must be a number'}), 400 
    
    new_expense = Expense(amount = amount, category = category, user_id = user_id)

    try:
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({ 'success': True, 'message': 'expense added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'database error'}), 500
'''
------------
ROUTE: EDIT EXPENSE
-----------
'''
@dashboard_bp.route('/api/expenses/<int:id>', methods = ['PUT'])
def editExpense(id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    amount = request.form.get('amount')
    category = request.form.get('category')

    if not amount or not category:
        return jsonify({'success': False, 'message': 'Amount and category required'}), 400
    
    try: 
        amount = float(amount)
    except ValueError:
        return jsonify({'success': False, 'message': 'Amount must be a number'}), 400
    try:
        expense = Expense.query.filter_by(id=id, user_id = user_id).first()
        if not expense:
            return jsonify({'success': False, 'message': 'Expense not found'}), 404 
        
        expense.amount = amount 
        expense.category = category

        db.session.commit()
        return jsonify({'success': True, 'message': 'expense updated successfully'}), 200 
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'database error'}), 500
'''
------------
ROUTE: DELETE EXPENSE
-----------
'''
@dashboard_bp.route('/api/expenses/<id>', methods = ['DELETE'])
def deleteExpense(id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401 
    
    expense = Expense.query.filter_by(id=id, user_id = user_id).first() 
    if not expense:
        return jsonify({'success': False, 'message': 'Expense not found'}), 404
    try:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Expense deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'database error'}), 500
'''
------------
ROUTE: GET EXPENSE
-----------
'''
@dashboard_bp.route('/api/expenses', methods = ['GET'])
def showExpenses():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    Expenses = Expense.query.filter_by(user_id = user_id).all()
    expense_list = []

    for expense in Expenses:
        expense_list.append({
            'id': expense.id,
            'amount': expense.amount,
            'category': expense.category
        })

    return jsonify({'success': True, 'expenses': expense_list}), 200
'''
------------
ROUTE: GET INCOME
-----------
'''
@dashboard_bp.route('/api/income', methods = ['GET'])
def getIncome():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401

    myIncome = Income.query.filter_by(user_id = user_id).first() 

    if not myIncome:
        return jsonify({'success': False, 'message': 'Income not found'}), 404  

    return jsonify({'success': True, 'income': myIncome.amount}), 200
'''
------------
ROUTE: EDIT INCOME
-----------
'''
@dashboard_bp.route('/api/income', methods = ['PUT'])
def changeIncome():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401 
    
    changeIncome = request.form.get('amount')
    try:
        changeIncome = float(changeIncome)
    except (ValueError, TypeError):
        return jsonify({'success': False, 'message': 'Income must be a number'}), 400
    
    myIncome = Income.query.filter_by(user_id = user_id).first()

    if not myIncome:
        return jsonify({'success': False, 'message': 'Income not found'}), 404
    
    try:
        myIncome.amount = changeIncome
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'income updated successfully'}), 200 
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'database error occurred'}), 500