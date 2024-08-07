from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), index = True, unique = True, nullable = False)
    password_hash = db.Column(db.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

        #ForeignKey to UserData
    userdata_id = db.Column(db.Integer, db.ForeignKey("userdata.id"))
    #Back references to userdata
    userdata = db.relationship("UserData", back_populates = "user")
    #One to One relationship with Profile
    profile = db.relationship("Profile", uselist = False, back_populates = "user")
    #One to Many relationship with CourseUser
    course_user = db.relationship("CourseUser", back_populates = "user")