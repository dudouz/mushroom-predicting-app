from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify, request
from logger import logger
from api.controllers.mushroom_controller import MushroomController
from api.models.mushroom_model import MushroomBody


mushroom_tags = Tag(name='Mushrooms', description='Operações relacionadas a API de cogumelos venenosos')

mushroom_routes = APIBlueprint('mushroom', __name__, abp_tags=[mushroom_tags])

@mushroom_routes.post('/api/evaluate', summary='Avalia um cogumelo', responses={
    "200": {"description": "Avaliação feita com sucesso"},
    "400": {"description": "Erro na requisição"},
    "500": {"description": "Erro no servidor"}
})
def evaluate(body: MushroomBody):
    body = request.json
    mushroom_controller = MushroomController(body)

    try:
        logger.info("Requisição de avaliação de cogumelo recebida")
        result = mushroom_controller.evaluate_mushroom()
        logger.info(f"Requisição de avaliação de cogumelo retornada: {result}")
        return jsonify({ 'result': result })
    except Exception as e:
        logger.error(f"Erro ao avaliar cogumelo: {e}")
        return jsonify({'error': str(e)}), 500