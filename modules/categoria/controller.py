from flask import Blueprint, request, jsonify
from modules.categoria.dao import DAOCategoria
from modules.categoria.modelo import Categoria
from modules.categoria.sql import SQLCategoria

categoria_controller = Blueprint('categoria_controller', __name__)
dao_categoria = DAOCategoria()
module_name = 'categoria'


def get_categorias():
    categorias = dao_categoria.get_all()
    results = [categoria.__dict__ for categoria in categorias]
    response = jsonify(results)
    response.status_code = 200
    return response


def create_categoria():
    data = request.json
    erros = []
    for campo in SQLCategoria._CAMPOS_OBRIGATORIOS:
        if campo not in data.keys() or not data.get(campo, '').strip():
            erros.append(f"O campo {campo} é obrigatorio")
    if dao_categoria.get_by_description(**data):
        erros.append(f"Já existe uma categoria com essa descrição")
    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    categoria = Categoria(**data)
    dao_categoria.salvar(categoria)
    response = jsonify('OK')
    response.status_code = 201
    return response


@categoria_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
def get_or_create_categorias():
    if request.method == 'GET':
        return get_categorias()
    else:
        return create_categoria()


@categoria_controller.route(f'/{module_name}/<id>/', methods=['GET'])
def get_categoria_by_id(id: int):
    print('id', id)
    return []
