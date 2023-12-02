# instala o pacote para obter o dataset:
from ucimlrepo import fetch_ucirepo
from pandas import read_csv
import pickle
import joblib

class  Loader:
    def __init__(self):
        pass

    def load_dataset(self, id):
        dataset_base = fetch_ucirepo(id=id)

        # verificar se a carga está correta, checando o nome do dataset
        print(f"Dataset loaded: {dataset_base.metadata.name}")

        data = read_csv(dataset_base.metadata.data_url)

        return data
    
    def load_model(self, model_name):
        if model_name.endswith('.pkl'):
             model = pickle.load(open(model_name, 'rb'))
        elif model_name.endswith('.joblib'):
            model = joblib.load(model_name)
        else:
            raise ValueError('Unsupported model file extension')
        return model