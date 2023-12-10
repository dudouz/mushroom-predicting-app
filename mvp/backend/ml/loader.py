# instala o pacote para obter o dataset:
from ucimlrepo import fetch_ucirepo
from pandas import read_csv
import pickle
import joblib

class  Loader:
    def load_dataset(self, id):
        dataset_base = fetch_ucirepo(id=id)

        # verificar se a carga está correta, checando o nome do dataset
        print(f"Dataset loaded: {dataset_base.metadata.name}")

        data = self.load_dataset_csv(dataset_base.metadata.data_url)

        return data
    
    def load_dataset_csv(self, csv_path):
        data = read_csv(csv_path)

        return data
    
    def load_model(self, model_path):
        if model_path.endswith('.pkl'):
             model = pickle.load(open(model_path, 'rb'))
        elif model_path.endswith('.joblib'):
            model = joblib.load(model_path)
        else:
            raise ValueError('Unsupported model file extension')
        return model
    
    def load_encoder(self, encoder_path):
        with open(encoder_path, 'rb') as f:
            encoder = pickle.load(f)
        return encoder
    
    def load_scaler(self, scaler_path):
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
        return scaler