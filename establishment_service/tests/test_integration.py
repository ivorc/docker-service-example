import sys
sys.path.insert(0,'..')

from tornado.test.web_test import WebTestCase
import app

class IntegrationTests(WebTestCase):
    def get_handlers(self):
        return app.get_handlers()

    def test_fetching_an_establishment(self):
        body = self.fetch("/establishment").body
        self.assertTrue(True)
