import json
from bson import ObjectId
from motor import MotorClient
from tornado import gen


class EstablishmentRepository:
    def __init__(self):
        self.client = MotorClient()

    @gen.coroutine
    def list_establishments(self):
        db = self.client.establishments
        cursor = db.establishments.find()
        result = yield cursor.to_list(1000)
        return result

    @gen.coroutine
    def insert_establishment(self, establishment):
        db = self.client.establishments

        app_id = yield db.establishments.insert(establishment.to_primitive())
        return str(app_id)

    @gen.coroutine
    def get_establishment(self, establishment_id: str):
        db = self.client.establishments
        cursor = db.establishments.find({"_id": ObjectId(establishment_id)})
        return (yield cursor.to_list(1000))
