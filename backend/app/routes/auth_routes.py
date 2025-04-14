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
@auth_bp.route('/signup', methods=['POST']) 
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']
    hashed_password = generate_password_hash(password)

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "error, username already taken"}), 409
    
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    session['user_id'] = new_user.id

    return jsonify({"message" : "signup successful"}), 201
'''
------------
ROUTE: LOGIN
-----------
'''
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login succesful"}), 200
    else:
        return jsonify({"error": "invalid credential"}), 401
   

@auth_bp.route('/logout', methods = ['GET'])
def logout():
    session.pop('user_id', None)
    return jsonify({'success': True, 'message': 'logged out successful'}), 200
