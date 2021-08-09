  
from flask import url_for
from flask_testing import TestCase

from service_2.app import app, names

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_food(self):

        for _ in range(20):
            response = self.client.get(url_for('enemy_gen'))

            text = response.data.decode().split(" ")
            self.assert200(response)
            assert any(word in response.data.decode() for word in names)