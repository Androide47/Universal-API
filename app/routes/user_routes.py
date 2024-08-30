from flask import Blueprint, jsonify, request
from app import db
from app.models import User

bp = Blueprint('user_routes', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201