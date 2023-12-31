# -*- coding: utf-8 -*-
"""Eduardo Rosa Iotti - MVP 4 - Engenharia de Sistemas Inteligentes [OK]

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_W8S-b9osjGstSGHoXa-s2bZCw-HZrHd

Imports

# Configuração **Inicial**
"""

# configuração para não exibir os warnings
import warnings
warnings.filterwarnings("ignore")

# Imports necessários
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# normalizador pras categorias qualitativas:
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# instala o pacote para obter o dataset:
!pip3 install -U ucimlrepo
from ucimlrepo import fetch_ucirepo

# instala pickle para exportar o modelo treinado:
import pickle

"""# Carregar **dados**"""

# adicionar o dataset Mushroom de id 73
# https://archive.ics.uci.edu/dataset/73/mushroom
dataset_base = fetch_ucirepo(id=73)

# verificar se a carga está correta, checando o nome do dataset
print(f"Dataset carregado: {dataset_base.metadata.name}")

data = pd.read_csv(dataset_base.metadata.data_url)

"""# Dividir em **conjuntos de teste** e **normalização dos dados**"""

# Define os eixos de características e alvo
# Nesse caso queremos descobrir se o cogumelo é venenos ou comestível
# Dessa forma removemos a coluna 'poisonous' de nosso dataframe ao declararmos as características
# E apontamos específicamente esta coluna como nosso alvo de predição.
X = data.drop('poisonous', axis=1)
y = data['poisonous']


# Como nossas colunas apresentam dados qualitativos representados por iniciais (ou algo similar)
# de cada # característica a ser avaliada, utilizaremos o LabelEncoder para nosso\
# alvo de predição (binário) e o OneHotEncoder para nossas colunas de características.

# Codificar os rótulos categóricos usando o LabelEncoder
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Codificar as características categóricas em X usando OneHotEncoder
onehot_encoder = OneHotEncoder(sparse=False, drop=None, handle_unknown='ignore')
X_encoded = onehot_encoder.fit_transform(X)

test_size = 0.20 # tamanho do conjunto de teste
seed = 7 # semente aleatória

# Dividir o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

# Parâmetros e partições da validação cruzada ten fold
scoring = 'accuracy'
num_particoes = 10
kfold = StratifiedKFold(n_splits=num_particoes, shuffle=True, random_state=seed) # validação cruzada com estratificação

"""# Modelagem e **inferência**"""

np.random.seed(7) # definindo uma semente global

# Lista que armazenará os modelos
models = []

# Criando os modelos e adicionando-os na lista de modelos
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# Listas para armazenar os resultados
results = []
names = []

# Mostramos os resultados da avaliação dos modelos
for name, model in models:
  cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
  results.append(cv_results)
  names.append(name)
  print(f"Modelo: {name}, Média: {cv_results.mean()}, Desvio: {cv_results.std()}")

# Geramos um gráfico boxplot para comparar os modelos visualmente:
fig = plt.figure(figsize=(15,10))
fig.suptitle('Boxplot comparativo entre modelos')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

"""# Avaliação dos modelos: **Montando e executando as pipelines de normalização e padronização**"""

np.random.seed(7) # definindo uma semente global para este bloco

# Listas para armazenar os armazenar os pipelines e os resultados para todas as visões do dataset
pipelines = []
results = []
names = []


# Criando os elementos do pipeline

# Algoritmos que serão utilizados
knn = ('KNN', KNeighborsClassifier())
cart = ('CART', DecisionTreeClassifier())
naive_bayes = ('NB', GaussianNB())
svm = ('SVM', SVC())

# Transformações que serão utilizadas
standard_scaler = ('StandardScaler', StandardScaler())
min_max_scaler = ('MinMaxScaler', MinMaxScaler())

# Montando os pipelines

# Dataset original
pipelines.append(('KNN-orig', Pipeline([knn])))
pipelines.append(('CART-orig', Pipeline([cart])))
pipelines.append(('NB-orig', Pipeline([naive_bayes])))
pipelines.append(('SVM-orig', Pipeline([svm])))

# Dataset Padronizado
pipelines.append(('KNN-padr', Pipeline([standard_scaler, knn])))
pipelines.append(('CART-padr', Pipeline([standard_scaler, cart])))
pipelines.append(('NB-padr', Pipeline([standard_scaler, naive_bayes])))
pipelines.append(('SVM-padr', Pipeline([standard_scaler, svm])))

# Dataset Normalizado
pipelines.append(('KNN-norm', Pipeline([min_max_scaler, knn])))
pipelines.append(('CART-norm', Pipeline([min_max_scaler, cart])))
pipelines.append(('NB-norm', Pipeline([min_max_scaler, naive_bayes])))
pipelines.append(('SVM-norm', Pipeline([min_max_scaler, svm])))

# Executando os pipelines
for name, model in pipelines:
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %.3f (%.3f)" % (name, cv_results.mean(), cv_results.std()) # formatando para 3 casas decimais
    print(msg)

# Boxplot de comparação dos modelos
fig = plt.figure(figsize=(25,6))
fig.suptitle('Comparação dos Modelos - Dataset orginal, padronizado e normalizado')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names, rotation=90)
plt.show()

"""# Otimização dos **Hiperparâmetros**"""

# Tuning do KNN

np.random.seed(7)

pipelines = []

# Definindo os componentes do pipeline
knn = ('KNN', KNeighborsClassifier())
standard_scaler = ('StandardScaler', StandardScaler())
min_max_scaler = ('MinMaxScaler', MinMaxScaler())

pipelines.append(('knn-orig', Pipeline(steps=[knn])))
pipelines.append(('knn-padr', Pipeline(steps=[standard_scaler, knn])))
pipelines.append(('knn-norm', Pipeline(steps=[min_max_scaler, knn])))

# Este param_grid_old foi criado para termos mais opções de parâmetros, porém gerou um resultado bem semelhante aos
# parametros sugeridos pelo exemplo mostrado em aula e apresentou um tempo de execução de 30 min, desta forma
# optei pela opção que executava mais rápido.

# param_grid_old = {
#     'KNN__n_neighbors': [5, 10, 15, 20],
#     'KNN__metric': ["euclidean", "manhattan", "minkowski"],
#     'KNN__weights': ['uniform', 'distance'],
#     'KNN__algorithm': ["auto", "ball_tree", "kd_tree", "brute"]
# }

param_grid = {
    'KNN__n_neighbors': [15, 20, 35, 50, 100],
    'KNN__metric': ["euclidean", "manhattan", "minkowski"],
}

# Prepara e executa o GridSearchCV
for name, model in pipelines:
    grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
    grid.fit(X_train, y_train)

    # Aponta a melhor configuração:
    print(f"Sem tratamento de missings: {name}")
    print(f"Melhor Score: {grid.best_score_} usando {grid.best_params_}")

    # Obtendo os melhores parâmetros encontrados
    best_params = grid.best_params_
    print(f"Melhores Parâmetros: {name}", best_params)

    # Avaliando o desempenho no conjunto de teste
    accuracy = grid.score(X_test, y_test)
    print(f"Acurácia no Conjunto de Teste: {name}", accuracy)

"""# **Finalização** do Modelo"""

# Preparação do modelo
scaler = StandardScaler().fit(X_train) # ajuste do scaler com o conjunto de treino
rescaledX = scaler.transform(X_train) # aplicação da padronização no conjunto de treino
model = KNeighborsClassifier(metric='euclidean', n_neighbors=5)
model.fit(rescaledX, y_train)

# Estimativa da acurácia no conjunto de teste
rescaledTestX = scaler.transform(X_test) # aplicação da padronização no conjunto de teste
predictions = model.predict(rescaledTestX)
print(accuracy_score(y_test, predictions))

# Preparação do modelo com TODO o dataset
onehot_encoder = OneHotEncoder(sparse=False, drop=None, handle_unknown='ignore')
X_encoded = onehot_encoder.fit_transform(X)

print(X_encoded)
print(X_encoded.astype(float))
scaler = StandardScaler().fit(X_encoded) # ajuste do scaler com TODO o dataset

rescaledX = scaler.transform(X_encoded) # aplicação da padronização com TODO o dataset
model.fit(rescaledX, y_encoded)

"""# Testando em **dados desconhecidos**"""

# Novos dados - não sabemos a classe!

new_mushroom_data = {
    'cap-shape': ['x', 'f'],
    'cap-surface': ['f', 'f'],
    'cap-color': ['g', 'n'],
    'bruises': ['f', 't'],
    'odor': ['f', 'n'],
    'gill-attachment': ['f', 'f'],
    'gill-spacing': ['c', 'c'],
    'gill-size': ['b', 'b'],
    'gill-color': ['g', 'w'],
    'stalk-shape': ['e', 't'],
    'stalk-root': ['b', 'b'],
    'stalk-surface-above-ring': ['k', 's'],
    'stalk-surface-below-ring': ['k', 's'],
    'stalk-color-above-ring': ['b', 'p'],
    'stalk-color-below-ring': ['n', 'p'],
    'veil-type': ['p', 'p'],
    'veil-color': ['w', 'w'],
    'ring-number': ['o', 'o'],
    'ring-type': ['l', 'p'],
    'spore-print-color': ['h', 'n'],
    'population': ['v', 'v'],
    'habitat': ['p', 'd']
}

# Definimos as colunas de características
columns = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']

# Normalizamos os dados tal qual fizemos no treinamento do modelo:
mushroom_dataframe = pd.DataFrame(new_mushroom_data, columns=columns)
mushroom_dataframe_encoded = onehot_encoder.transform(mushroom_dataframe)
mushroom_dataframe_scaled = scaler.transform(mushroom_dataframe_encoded)

print(mushroom_dataframe_encoded)

# Padronização nos dados de entrada usando o mesmo scaler utilizado em X anteriormente
X_Input = mushroom_dataframe_scaled.astype(float)
XInputRescaled = scaler.transform(X_Input)

print(XInputRescaled)

# Predição de classes dos dados de entrada
output = model.predict(XInputRescaled)

# 0 venenoso 1 comestível
print(output)

"""# **Exportando** O Modelo"""

# Declaramos aqui o nome do modelo, caminho local a salvarmos o arquivo
# Assim como toda lógica para exportar o modelo treinado usando o pickle:

model_name = "Modelo Treinado - Eduardo Rosa Iotti - KNN - Mushrooms"

pkl_artifact_filename = f"{model_name}.pkl"

pkl_local_path = f"/content/{pkl_artifact_filename}"
with open(pkl_local_path, "wb") as model_file:
  pickle.dump(model, model_file)

# Exportamos tambem os normalizadores, para trabalhar com dados novos seguindo
# o mesmo encoding dos dados categóricos:

with open('onehot_encoder.pkl', 'wb') as f:
    pickle.dump(onehot_encoder, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

"""# **Conclusões** gerais

Bom, primeiramente, para mim este MVP foi o mais desafiador de todos, pois se tratava de um assunto totalmente novo para mim.

Pude aprender bastante, mas acredito que se quiser seguir atuando nessa área específica, tenho um imenso caminho pela frente.

## A **proposta**

A ideia aqui foi utilizar um dataset de cogumelos para trazer uma predição da possibilidade dele ser comestível, baseado em suas características biológicas.

## Um **grande desafio**

Acredito que o ponto crucial aqui neste modelo é que os dados são categóricos e não quantitativos, por conta disso o desafio se tornou um pouco maior do que eu esperava.

Além disso são 22 colunas de dados categóricos o que torna um pouco extensivo o teste, principalmente ao criar novos objetos a serem avaliados pelo modelo.

Para sobrepor este desafio, precisei buscar uma solução de normalização dos dados, tanto de forma binária para a classe, quanto de forma decimal para as características.

## **Construção e organização** dos dados

 Para uma avaliação robusta, conforme sugerido em aula adotei uma validação cruzada com 10 partições estratificadas - ten fold.

 Fazendo isso pude garantir que meu modelo foi exposto a diferentes conjuntos organizados de forma a evitar falsos positivos.

## A Escolha do **modelo**

Acabei optando pelo KNN que apresentou uma acurácia altíssima, tanto no tuning final quanto no treinamento.


### O **fine tuning**: parâmetros diferentes

No fine tuning eu divergi um pouco da orientação inicial, buscando expandir as alternativas e provocar o modelo para me trazer diferentes scores.

Pesquisei um pouco na documentação e busquei explorar alguns parâmetros adicionais no tuning do KNN e obtive uma acurácia semelhante em todos os resultados, porém deixou este bloco um pouco demorado para ser executado: aproximadamente 30 minutos.

Ao diminuir estes parametros e seguir algo mais próximo à orientação da aula, obtive resultados bem semelhantes e com tempo menor de execução. Priorizei esse setup mas mantive comentado o segundo param grid para fins ilustrativos.

### **Fine tuning 2**: número de vizinhos considerados

Ainda nessa ideia de experimentar percebi que o KNN ainda estava sempre considerando o menor numero de vizinhos possível, e que
usar somente 1 vizinho pode trazer problemas de classificação, por termos uma base com mais de 8 mil exemplos, decidi aumentar o numero de vizinhos e o número final ficou 15 que é o menor número dentre as alternativas testadas.

## Os **problemas** encontrados

Ao confrontar o banco com dados novos tive alguns problemas com os dados categóricos. Algumas classificações eram consideradas desconhecidas pelo modelo e isso quebrava a predição.

Utilizei um parâmetro no encoder das colunas de categorias para ignorar em caso de dados desconhecidos e o resultado foi satisfatório: ao testar com dados que sabíamos sua classe o sistema pareceu gerar resultados confiáveis.

## Exports **complementares**

Por fim, ao aplicar o modelo no meu sistema compreendi que precisaria utilizar os encoders e scalers já ajustados com os dados para normalizar, também, o input do usuário.

## Sobre a **predição**

Eu acredito que a predição está interessante, pois qualquer dado divergente de uma classificação muito próxima da classe comestível já é considerada venenosa.
"""