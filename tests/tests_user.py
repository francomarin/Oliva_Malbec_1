import unittest
import os
from app import db, create_app
from app.models.user import User

class TestUserModel(unittest.TestCase):

    def setUp(self):
        os.environ["FLASK_CONTEXT"] = "testing"
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.rollback()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(email = "test@test.com")
        user.set_password("test")
        db.session.add(user)
        db.session.commit()

        fetched_user = User.query.filter_by(email = "test@test.com").first()
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.email, "test@test.com")
        self.assertTrue(fetched_user.check_password("test"))

if __name__ == "__main__":
    unittest.main()