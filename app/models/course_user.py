from app import db

class CourseUser(db.Model):
    __tablename__ = "course-user"

    id = db.Column(db.Integer, primary_key = True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    grade = db.Column(db.String(4), nullable = True)