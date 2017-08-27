from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return  {'message': 'Store not found'}, 404

class StoreList(Resource):
    def get(self):
        print('fuck off')
        return {'stores': [store.json() for store in StoreModel.query.all()]}
