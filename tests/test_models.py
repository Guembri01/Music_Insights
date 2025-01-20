import unittest
import pandas as pd
from app.models import load_data, analyze_genre_popularity, analyze_music_features_by_genre
from app import create_app, cache

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a Flask app and initialize the cache
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['CACHE_TYPE'] = 'SimpleCache'
        cache.init_app(cls.app)

        # Load the dataset once for all tests
        with cls.app.app_context():
            cls.df = load_data()

    def test_load_data(self):
        # Test if the dataset is loaded correctly
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertGreater(len(self.df), 0)

    def test_analyze_genre_popularity(self):
        # Test the analyze_genre_popularity function
        with self.app.app_context():
            graphJSON, interpretation = analyze_genre_popularity(self.df)
            self.assertIsInstance(graphJSON, str)
            self.assertIsInstance(interpretation, str)
            self.assertGreater(len(graphJSON), 0)
            self.assertGreater(len(interpretation), 0)

    def test_analyze_music_features_by_genre(self):
        # Test the analyze_music_features_by_genre function
        with self.app.app_context():
            graphJSON, interpretation = analyze_music_features_by_genre(self.df, 'danceability')
            self.assertIsInstance(graphJSON, str)
            self.assertIsInstance(interpretation, str)
            self.assertGreater(len(graphJSON), 0)
            self.assertGreater(len(interpretation), 0)

if __name__ == '__main__':
    unittest.main()