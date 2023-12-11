import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from ml.loader import Loader

class Preprocessor:
    def normalize_dataframe(self, X, y):
        # Carregar onehot_encoder e scaler pré-treinados
        loader = Loader()
        scaler = loader.load_scaler('ml/model/scaler_ok.pkl')
        onehot_encoder = loader.load_encoder('ml/model/onehot_encoder_ok.pkl')

        # Codificar a classe, pois ela é categórica
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)

        # Codificar as variáveis categóricas
        X_encoded = onehot_encoder.transform(X)

        # A normalização é necessária para um resultado otimizado acima dos 98% de acurácia
        X_scaled = scaler.fit_transform(X_encoded)

        return X_scaled, y_encoded

    def prepare_holdout(self, data, test_size, seed):
        X = data.drop('poisonous', axis=1)
        y = data['poisonous']

        X_scaled, y_encoded = self.normalize_dataframe(X, y)

        return train_test_split(X_scaled, y_encoded, test_size=test_size, random_state=seed)
        
    def pre_process(self, data):
        X_train, X_test, y_train, y_test = self.prepare_holdout(data, 0.2, 42)

        return X_train, X_test, y_train, y_test
    
    def normalize_input(self, data):
        columns = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']

        # Carregar onehot_encoder e scaler pré-treinados
        loader = Loader()
        scaler = loader.load_scaler('ml/model/scaler_ok.pkl')
        onehot_encoder = loader.load_encoder('ml/model/onehot_encoder_ok.pkl')

        dataframe = pd.DataFrame(data, columns=columns)
        dataframe_encoded = onehot_encoder.transform(dataframe)
        dataframe_scaled = scaler.transform(dataframe_encoded)

        X_Input = dataframe_scaled.astype(float)
        XInputRescaled = scaler.transform(X_Input)

        return XInputRescaled