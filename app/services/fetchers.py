from flask import jsonify
from app.models.course import Course
from app.models.user import User
from app.models.userData import UserData

def fetch_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        raise Exception('Course not found')
    return course

def fetch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        raise Exception('User not found')
    return user

def fetch_userData(user_id):
    user_data = UserData.query.filter_by(user_id=user_id).first()
    return user_data