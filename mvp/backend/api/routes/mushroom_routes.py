from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify, request
from logger import logger
from api.controllers.mushroom_controller import evaluate_mushroom

mushroom_tags = Tag(name='Mushrooms', description='Operações relacionadas a API de cogumelos venenosos')

mushroom_routes = APIBlueprint('mushroom', __name__, abp_tags=[mushroom_tags])

@mushroom_routes.post('/api/evaluate', summary='Avalia um cogumelo', responses={
    "200": {"description": "Avaliação feita com sucesso"},
    "400": {"description": "Erro na requisição"},
    "500": {"description": "Erro no servidor"}
})
def evaluate():
    try:
        data = request.json
        logger.info("Requisição de avaliação de cogumelo recebida")
        result = evaluate_mushroom(data)
        logger.info(f"Requisição de avaliação de cogumelo retornada: {result}")
        return jsonify({ 'result': result })
    except Exception as e:
        logger.error(f"Erro ao avaliar cogumelo: {e}")
        return jsonify({'error': str(e)}), 500