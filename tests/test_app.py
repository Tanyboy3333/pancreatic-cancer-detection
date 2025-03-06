import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_prediction(self):
        tester = app.test_client(self)
        response = tester.post('/predict', data=dict(
            feature1=5.9,
            feature2=3.0,
            feature3=4.2,
            feature4=1.5
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'prediction', response.data)

if __name__ == '__main__':
    unittest.main()
