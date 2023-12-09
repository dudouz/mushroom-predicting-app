import numpy as np
from ml.preprocessor import Preprocessor
from utils import Utils

class Predictor:
    def predict(self, model, data):
        utils = Utils()
        preprocessor = Preprocessor()

        data_converted = utils.convert_spinalcase(data)

        data_normalized = preprocessor.normalize_input(data_converted)

        result = model.predict(data_normalized)
        if result[0] == 1:
            return 'Poisonous'
        else:
            return 'Edible'
