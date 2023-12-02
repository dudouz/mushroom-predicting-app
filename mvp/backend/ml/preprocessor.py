import pandas as pd
import pickle

from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

class Preprocessor:
    def normalize_dataframe(self, data):
        columns = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']

        # Carregar onehot_encoder e scaler pré-treinados
        with open('ml/model/onehot_encoder.pkl', 'rb') as f:
            onehot_encoder = pickle.load(f)

        with open('ml/model/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        dataframe = pd.DataFrame(data, columns=columns)

        dataframe_encoded = onehot_encoder.transform(dataframe)
        dataframe_scaled = scaler.transform(dataframe_encoded)

        X_Input = dataframe_scaled.astype(float)
        XInputRescaled = scaler.transform(X_Input)

        return XInputRescaled