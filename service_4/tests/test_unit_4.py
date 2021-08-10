from flask import url_for
from flask_testing import TestCase

from service_4.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_winner(self):

        payload = ["Evan Almighty",5,5], ["Jack the ripper", 6, 5]
        response = self.client.post(url_for('who_won'), json=payload)


        self.assert200(response)
        
        self.assertEqual(response.json, "Loss")



    def testloser(self):

        payload = ["Evan Almighty",5,5], ["Jack the ripper", 5, 5]
        response = self.client.post(url_for('who_won'), json=payload)


        self.assert200(response)
        
        self.assertEqual(response.json, "Win")