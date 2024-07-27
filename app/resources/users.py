from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from app.models.userData import UserData
from app.models.role import Role
from app.models.profile import Profile

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods = ["POST"])
def create_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    role_name = data.get("role")
    
    #Validations
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400
    
    if User.query.filter_by(email = email).first():
        return jsonify({"message": "Email already registered"}), 400
    
    role = Role.query.filter_by(name = role_name).first()
    if not role:
        return jsonify({"message": "Role not found"}), 400

    #User Data creation for User
    user_data = UserData(
        first_name = None,
        last_name = None,
        dni = None,
        phone = None,
        address = None,
    )
    db.session.add(user_data)
    db.session.commit()
    
    #User creation
    user = User(email = email, userdata = user_data)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    #Profile creation for User
    profile = Profile(user_id = user.id, role_id = role.id)
    db.session.add(profile)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "id": user.id}), 201

@user_bp.route("/users", methods = ["GET"])
def get_all_users():
    users = User.query.all()
    users_list = []
    for user in users:
        data = {
            "id" : user.id,
            "email" : user.email,
            "first_name" : user.userdata.first_name,
            "last_name" : user.userdata.last_name
        }
        users_list.append(data)
    return jsonify({"users": users_list}), 200