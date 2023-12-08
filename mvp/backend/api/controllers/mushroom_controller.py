import api.schemas.mushroom_schema as MushroomSchema
from flask import jsonify
from stringcase import snakecase
from ml.predictor import Predictor
from ml.loader import Loader
import numpy as np
from utils import Utils

class MushroomController:
    def __init__(self, data):
        self.data = data

    def evaluate_mushroom(self):
        utils = Utils()
        print('evaluate_mushroom')
        loader = Loader()
        predictor = Predictor()

        model = loader.load_model('ml/model/modelo_eduardo_mushrooms.pkl')
        
        new_data = utils.convert_snakecase(self.data)
        
        data_serialized = MushroomSchema.MushroomSchema(**new_data)

        data_converted = utils.convert_data_to_array(data_serialized.dict())

        result = predictor.predict(model, data_converted)
        
        return result