import json
from unittest import TestCase
from unittest.mock import MagicMock
from tornado import gen
from tornado.concurrent import Future

__author__ = 'adrian'

class EstablishmentHandlerTests(TestCase):
    @gen.coroutine
    def test_that_establishments_can_be_listed(self):
        # Arrange

        expected_data = {'some': 'data'}

        mock_establishment_repository = EstablishmentRepository()
        future = Future()
        future.set_result(expected_data)
        mock_establishment_repository.list_establishments = MagicMock(return_value=future)

        request = MagicMock()
        application = MagicMock()
        output = MagicMock()
        handler = app.EstablishmentHandler(application, request,
            establishment_repository=mock_establishment_repository)
        handler.write = output

        # Act
        yield handler.get()

        # Assert
        output.assert_called_once_with(json.dumps(expected_data))


if __name__ == '__main__':
    unittest.main()
