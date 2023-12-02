from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, jsonify, redirect
from logger import logger
from flask_cors import CORS
from flask_sslify import SSLify
import warnings
warnings.filterwarnings("ignore")

# importar rotas
from api.routes.mushroom_routes import mushroom_routes

# definir tags da doc
mushroom_tags = Tag(name='Mushroom', description='Documentação da API de Classificação do Cogumelos')

info = Info(title="Mushroom Classifier", version="1.0.0")
app = OpenAPI(__name__, info=info)

sslify = SSLify(app)

# registrar rotas
app.register_api(mushroom_routes)

CORS(app)

@app.get('/')
def home():
    return jsonify({'message': 'Hello Mushroom lover!'})