from ml.predictor import Predictor
from ml.loader import Loader
from ml.preprocessor import Preprocessor
from ml.evaluator import Evaluator

# Instanciação das Classes
loader = Loader()
evaluator = Evaluator()
predictor = Predictor()
preprocessor = Preprocessor()

# Parâmetros
# Dataset utilizado: https://archive.ics.uci.edu/dataset/73/mushroom    
dataset_id = 73
test_data = loader.load_dataset_csv('ml/data/mushroom-data-golden.csv')
columns = test_data.columns.to_list()

# Testes básicos
def test_data_loader():
    data = loader.load_dataset(dataset_id)
    assert data.shape[1] == 23

def test_model_loader():
    model_path = 'ml/model/modelo_eduardo_mushrooms.pkl'
    model = loader.load_model(model_path)
    assert model is not None

def test_column_names():
    assert columns == ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat', 'poisonous']

# Teste do modelo

# Critérios
# Acurácia: % de acertos
# Recall: % de positivos corretamente identificados
# Precisão: % de positivos entre os identificados
# F1: média harmônica entre recall e precisão

min_accuracy = 0.98
min_recall = 0.98
min_precision = 0.98
min_f1 = 0.98

# Testar Modelo
def test_knn():
   #Importamos o modelo:
   model_path = 'ml/model/modelo_eduardo_mushrooms.pkl'
   model = loader.load_model(model_path)

   X = test_data.drop('poisonous', axis=1)
   y = test_data['poisonous']

   # Preprocessamos os dados - para normalizar as colunas categóricas:
   X_scaled, y_encoded = preprocessor.normalize_dataframe(X, y)
   
   # Avaliamos o modelo:
   evaluator = Evaluator()
   accuracy, recall, precision, f1 = evaluator.evaluate_model_scores(model, X_scaled, y_encoded)

   # Testamos as métricas:
   assert accuracy >= min_accuracy
   assert recall >= min_recall
   assert precision >= min_precision
   assert f1 >= min_f1     

    

