import unittest
from app import app, db

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_create_user(self):
        response = self.app.post('/users', json={'name': 'John Doe', 'email': 'john@example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('John Doe', response.get_data(as_text=True))

    def test_get_users(self):
        self.app.post('/users', json={'name': 'Jane Doe', 'email': 'jane@example.com'})
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Jane Doe', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
