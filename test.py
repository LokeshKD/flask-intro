from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # Ensure Flask is set-up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure login page loads correctly.
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # TestCase for correct login credentials
    def test_login_correct_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'You were just logged in', response.data)

    # TestCase for incorrect login credentials
    def test_login_incorrect_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='adin'),
            follow_redirects=True
        )
        self.assertIn(b'Invalid Credentials', response.data)

    # TestCase for logout.
    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were just logged out', response.data)


if __name__ == '__main__':
  unittest.main()
