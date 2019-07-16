#Imports

import unittest
from flask_testing import TestCase
from project import app, db
from project.models import User, BlogPost

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "admin@domain.com", "admin"))
        db.session.add(BlogPost("Test post", "This is a test. Only a test."))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):
    # Ensure Flask is set-up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure login page loads correctly.
    def test_login_page(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # TestCase for correct login credentials
    def test_login_correct_credentials(self):
        response = self.client.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'You were just logged in', response.data)

    # TestCase for incorrect login credentials
    def test_login_incorrect_credentials(self):
        response = self.client.post(
            '/login',
            data=dict(username='admin', password='adin'),
            follow_redirects=True
        )
        self.assertIn(b'Invalid Credentials', response.data)

    # TestCase for logout.
    def test_logout(self):
        self.client.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'You were just logged out', response.data)


if __name__ == '__main__':
  unittest.main()
