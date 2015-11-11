import json
from bson import json_util
from tornado import gen
from tornado.web import RequestHandler
from establishment_repository import EstablishmentRepository


class EstablishmentHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        if False:
            # These are the fields, but initialize is called
            # prior to __init__
            self.establishment_repository = None


    def initialize(self, establishment_repository: EstablishmentRepository):
        # injection of arguments from the handler configuration is done
        # here.
        """

        :type establishment_repository: EstablishmentRepository
        """
        assert isinstance(establishment_repository, EstablishmentRepository)
        self.establishment_repository = establishment_repository


    def data_received(self, chunk):
        pass


    @gen.coroutine
    def get(self, establishment_id=None):
        if establishment_id:
            establishment = yield self.establishment_repository.get_establishment(establishment_id)
            j = json.dumps(establishment, default=json_util.default)
            self.write(j)
        else:
            establishment_list = yield self.establishment_repository.list_establishments()
            j = json.dumps(establishment_list, default=json_util.default)
            self.write(j)


    @gen.coroutine
    def put(self):
        data = json.loads(self.request.body.decode('utf-8'))
        #TODO: Validate the data structure
        establishment_id = yield self.establishment_repository.insert_establishment(data)
        self.write(json.dumps({"id": establishment_id,}))


    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
