from flask import Blueprint, jsonify, request
from app.models import db, User  # Ensure User is defined in your models.py

# Create the blueprint
user_routes = Blueprint('user_routes', __name__)

# Example route: Fetch all users
@user_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        user_list = [{"id": user.id, "name": user.name} for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Example route: Create a new user
@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    try:
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "user": {"id": new_user.id, "name": new_user.name}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Example route: Fetch a specific user
@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"id": user.id, "name": user.name}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
