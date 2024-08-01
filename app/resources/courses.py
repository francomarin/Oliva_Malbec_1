from flask import Blueprint, request, jsonify
from app import db
from app.models.course import Course 
from app.services.fetchers import *

course_bp = Blueprint("course", __name__)

@course_bp.route("/courses", methods = ["POST"])
def create_course():
    try:
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
    except Exception as e:
        return jsonify({"message": str(e)}), 404

@course_bp.route("/courses", methods = ["GET"])
def get_all_courses():
    try:
        courses = Course.query.all()
        courses_list = []
        for course in courses:
            data = {
                "id" : course.id,
                "name" : course.name
            }
            courses_list.append(data)
        return jsonify({"courses": courses_list}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404

@course_bp.route("/courses/<int:course_id>", methods = ["GET"])
def get_course_by_id(course_id):
    try:
        course = fetch_course(course_id)

        data = {
            "id" : course.id,
            "name" : course.name
        }
        return jsonify({"course": data}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404

@course_bp.route("/courses/<int:course_id>", methods = ["PUT"])
def update_course(course_id):
    try:
        course = Course.query.filter_by(id = course_id).first()

        if not course:
            return jsonify({"message": "Course not found"}), 400

        data = request.get_json()

        course.name = data["name"]

        db.session.commit()
        return jsonify({"message": "Course updated successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404

@course_bp.route("/courses/<int:course_id>", methods = ["DELETE"])
def delete_course(course_id):
    try:
        course = Course.query.filter_by(id = course_id).first()

        if not course:
            return jsonify({"message": "Course not found"}), 400

        db.session.delete(course)
        db.session.commit()
        return jsonify({"message": "Course deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404