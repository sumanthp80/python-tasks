import unittest
import warnings
from app import app
from urllib.parse import urlsplit

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=DeprecationWarning)
            response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()

