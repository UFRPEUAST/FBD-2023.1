# Connect to your postgres DB
from datetime import datetime, timedelta
import random

import psycopg2
from faker import Faker

#
# fake = Faker()
# from sql import insert_item
#
conf = dict(
    dbname="estoque_fbd_2023_1",
    user="postgres", password="postgres",
    host="localhost", port="5432"
)
# conn = psycopg2.connect(**conf)
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM produto")
# cols = [desc[0] for desc in cursor.description]
# results = cursor.fetchall()
# results = [dict(zip(cols, i)) for i in results]
# print(results)
# pc = {
#     'coca-cola': 2,
#     'cafe': 6,
#     'arroz': 4,
# }
#
# for i, produto in enumerate(results):
#     item = random.randint(1, 20)
#     for j in range(item):
#         num = i + 1
#         cod_barra = '{}{}{}'.format(num, j, produto.get('id'))
#         numero_lote = cod_barra
#         data_entrada = datetime.now()
#         day = random.randint(1, 100)
#         data_validade = data_entrada + timedelta(days=day)
#         data_validade = data_validade.date()
#         quantidade = random.randint(1, 100)
#         preco_compra = pc.get(produto.get('nome'), 5)
#         preco_venda = preco_compra + 4
#         produto_id = produto.get('id')
#         data = [
#             cod_barra, numero_lote, data_entrada,
#             data_validade, quantidade, preco_compra, preco_venda,
#             produto_id
#         ]
#         sql = insert_item(*data)
#         print(sql)
#         cursor.execute(sql)
#         conn.commit()
#


from flask import Flask, jsonify, Response, make_response, request

app = Flask(__name__)


@app.route('/produto/', methods=['POST', 'GET'])
def produtos():
    if request.method == 'GET':
        conn = psycopg2.connect(**conf)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produto")
        cols = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()
        results = [dict(zip(cols, i)) for i in results]
        response = jsonify(results)
        response.status_code = 200
        return response
    if request.method == 'POST':
        response = jsonify('OK')
        response.status_code = 201
        # produto = request.json
        return response


@app.route('/marca/', methods=['POST', 'GET'])
def marcas():
    if request.method == 'GET':
        conn = psycopg2.connect(**conf)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM marca")
        cols = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()
        results = [dict(zip(cols, i)) for i in results]
        response = jsonify(results)
        response.status_code = 200
        return response
    if request.method == 'POST':
        response = jsonify('OK')
        response.status_code = 201
        marca = request.json
        #antes de salvar,
        #devemos verificar se já existe uma marca com o cnpj
        slq = ("insert into marca(nome, cnpj) "
               "values('{}', '{}')".
               format(marca.get('nome'),
                      marca.get('cnpj')))
        conn = psycopg2.connect(**conf)
        cursor = conn.cursor()
        cursor.execute(slq)
        conn.commit()
        print(marca)
        return response
