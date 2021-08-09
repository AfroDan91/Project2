  
from flask import url_for
from flask_testing import TestCase

from app import app, names

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_food(self):

        for _ in range(20):
            response = self.client.get(url_for('enemy_gen'))

            #self.assert200(response)
            #self.assertIn(response.data.decode(), names)
            #assert "Jack the ripper" or "Angry Dave" in response.data.decode()