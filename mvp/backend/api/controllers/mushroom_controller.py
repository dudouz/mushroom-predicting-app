import api.schemas.mushroom_schema as MushroomSchema
from flask import jsonify
from stringcase import snakecase
from ml.predictor import Predictor
from ml.loader import Loader
import numpy as np

class MushroomController:
    def __init__(self, data):
        self.data = data

    def evaluate_mushroom(self):
        print('evaluate_mushroom')
        loader = Loader()
        predictor = Predictor()

        model = loader.load_model('ml/model/modelo_eduardo_mushrooms.pkl')
        
        new_data = self.convert_case(self.data)
        
        data_serialized = MushroomSchema.MushroomSchema(**new_data)

        data_converted = self.convert_data_to_array(data_serialized.dict())

        result = predictor.predict(model, data_converted)
        
        return result

    def convert_case(self, object):
        new_object = {}
        for key in object:
            new_object[snakecase(key)] = object[key]

        return new_object

    def convert_data_to_array(self, data):
        new_data = {}

        for key in data:
            new_data[snakecase(key)] = [data[key]]

        return new_data