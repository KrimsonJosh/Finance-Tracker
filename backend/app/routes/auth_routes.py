from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return "Hello world"
'''
------------
ROUTE: SIGNUP
-----------
'''
@auth_bp.route('/signup', methods=['GET', 'POST']) 
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id

        return redirect(url_for('auth.home')) # TODO : add sessions
    return render_template('auth_templates/signup.html')
'''
------------
ROUTE: LOGIN
-----------
'''
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('auth.home')) # TODO : add sessions
        else:
            return "Invalid Username or password", 401 
    return render_template('auth_templates/login.html')

@auth_bp.route('/logout', methods = ['GET'])
def logout():
    session.pop('user_id', None)
    return jsonify({'success': True, 'message': 'logged out successful'}), 200
