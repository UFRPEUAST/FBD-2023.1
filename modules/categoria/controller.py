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
    categoria = dao_categoria.salvar(categoria)
    print(categoria)
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

# def produtos():
#     if request.method == 'GET':
#         conn = psycopg2.connect(**conf)
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM produto")
#         cols = [desc[0] for desc in cursor.description]
#         results = cursor.fetchall()
#         results = [dict(zip(cols, i)) for i in results]
#         response = jsonify(results)
#         response.status_code = 200
#         return response
#     if request.method == 'POST':
#         response = jsonify('OK')
#         response.status_code = 201
#         # produto = request.json
#         return response
