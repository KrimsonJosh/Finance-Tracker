from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
from ..models import db, Expense, Income

dashboard_bp = Blueprint('dashboard', __name__)

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
        user_id = session.get('user_id')
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

@dashboard_bp.route('/api/expenses/<id>', methods = ['DELETE'])
def deleteExpense(id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401 
    
    expense = Expense.query.filter_by(id=id, user_id = user_id).first() 
    if not expense:
        return jsonify({'sucesss': False, 'message': 'Expense not found'}), 404
    try:
        db.session.delete(expense)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'database error'}), 500
    

@dashboard_bp.route('/api/expenses', methods = ['GET'])
def showExpenses():
    user_id = session.get('user_id')

@dashboard_bp.route('/api/income', methods = ['PUT'])
def changeIncome():
    pass 

