import numpy as np
from ml.preprocessor import Preprocessor
from utils import Utils

class Predictor:
    def predict(self, model, data):
        utils = Utils()
        preprocessor = Preprocessor()

        normalized_columns_names = utils.convert_spinalcase(data)

        data_converted = preprocessor.normalize_dataframe(normalized_columns_names)

        result = model.predict(data_converted)
        if result[0] == 1:
            return 'Poisonous'
        else:
            return 'Edible'
