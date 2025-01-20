import unittest
from flask_testing import TestCase
from app import create_app, cache

class TestRoutes(TestCase):
    def create_app(self):
        # Create the Flask app for testing
        app = create_app()
        app.config['TESTING'] = True
        app.config['CACHE_TYPE'] = 'SimpleCache'  # Use SimpleCache for testing
        return app

    def setUp(self):
        # Clear the cache before each test
        cache.clear()

    def test_index_route(self):
        # Test the index route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenue', response.data)  # Adjust based on your index.html content

    def test_dashboard_route(self):
        # Test the dashboard route
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tableau de Bord', response.data)  # Adjust based on your dashboard.html content

if __name__ == '__main__':
    unittest.main()