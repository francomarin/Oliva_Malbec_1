from flask import Blueprint, request, jsonify
from app import db
from app.models.course import Course 

course_bp = Blueprint("course", __name__)

@course_bp.route("/courses", methods = ["POST"])
def create_course():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"message": "Course name is required"}), 400

    if Course.query.filter_by(name = name).first():
        return jsonify({"message": "Course already registered"}), 400

    course = Course(name = name)
    db.session.add(course)
    db.session.commit()
    return jsonify({"message": "Course registered successfully", "id": course.id}), 201