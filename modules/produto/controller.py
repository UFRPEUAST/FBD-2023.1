from flask import Blueprint

produto_controller = Blueprint('produto_controller', __name__)

module_name = 'produto'


@produto_controller.route(f'/{module_name}/', methods=['GET'])
def get_produto():
    print('produtos')
    return []


@produto_controller.route(f'/{module_name}/<id>/', methods=['GET'])
def get_produto_by_id(id: int):
    print('id', id)
    return []
