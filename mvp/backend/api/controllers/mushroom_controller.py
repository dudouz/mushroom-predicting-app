import api.schemas.mushroom_schema as MushroomSchema
from flask import jsonify
from stringcase import snakecase
from ml.predictor import Predictor
from ml.loader import Loader
import numpy as np

def evaluate_mushroom(data):
    print('evaluate_mushroom')
    loader = Loader()
    predictor = Predictor()

    model = loader.load_model('ml/model/modelo_eduardo_mushrooms.pkl')
    
    new_data = convert_case(data)
    
    data_serialized = MushroomSchema.MushroomSchema(**new_data)

    data_converted = convert_data_to_array(data_serialized.dict())

    result = predictor.predict(model, data_converted)
    
    return result

def convert_case(object):
    new_object = {}
    for key in object:
        new_object[snakecase(key)] = object[key]

    return new_object

def convert_data_to_array(data):
    new_data = {}

    for key in data:
        new_data[snakecase(key)] = [data[key]]

    return new_data