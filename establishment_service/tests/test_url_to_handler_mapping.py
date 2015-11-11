from asyncio.test_utils import TestCase
import json
from unittest.mock import MagicMock, Mock
from tornado.test.web_test import WebTestCase
import app

__author__ = 'adrian'

import unittest


class UrlMatchingTests(TestCase):
    def find_handler(self, handlers, url):
        for handler in handlers:
            if handler.regex.match(url):
                return handler.handler_class
        return None

    def test_that_the_establishment_handler_handles_the_establishment_resource(self):
        handler = self.find_handler(app.get_handlers(), '/establishment/')
        self.assertEqual(handler, app.EstablishmentHandler)


if __name__ == '__main__':
    unittest.main()
