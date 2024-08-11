from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app import db
from app.services.fetchers import fetch_user_by_email

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods = ["POST"])
def login():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]

        user = fetch_user_by_email(email)

        if not user.check_password(password):
            return jsonify({"message": "Invalid password"}), 401

        access_token = create_access_token(identity = {"id": user.id, "role": user.profile.role.name})
        return jsonify(access_token = access_token), 200
    except KeyError as e:
        return jsonify({"message": f"{str(e)} is required"})
    except Exception as e:
        return jsonify({"message": str(e)}), 400