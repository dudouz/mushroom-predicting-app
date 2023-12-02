import numpy as np
from ml.preprocessor import Preprocessor
from stringcase import spinalcase


class Predictor:
    def predict(self, model, data):
        preprocessor = Preprocessor()

        normalized_columns_names = self.convert_case(data)

        data_converted = preprocessor.normalize_dataframe(normalized_columns_names)

        result = model.predict(data_converted)
        if result[0] == 1:
            return 'Poisonous'
        else:
            return 'Edible'

        
    def convert_case(self, object):
        new_object = {}
        for key in object:
            new_object[spinalcase(key)] = object[key]

        return new_object