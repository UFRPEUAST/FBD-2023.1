from flask import Blueprint

marca_controller = Blueprint('marca_controller', __name__)

@marca_controller.route('/marca/', methods=['GET'])
def get_marca():
    print('marcas')
    return []


@marca_controller.route('/marca/<id>/', methods=['GET'])
def get_marca_by_id(id: int):
    print('id', id)
    return []

