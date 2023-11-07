from modules.categoria.sql import SQLCategoria
from modules.marca.sql import SQLMarca


class SQLProduto:
    _TABLE_NAME = 'produto'
    _COL_ID = 'id'
    _COL_NOME = 'nome'
    _COL_MARCA_ID = 'marca_id'
    _COL_CATEGORIA_ID = 'categoria_id'
    _REFERENCES_MARCA = f'{SQLMarca._TABLE_NAME}({SQLMarca._COL_ID})'
    _REFERENCES_CATEGORIA = f'{SQLCategoria._TABLE_NAME}({SQLCategoria._COL_ID})'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'(id serial primary key, ' \
                    f'{_COL_NOME} varchar(255), ' \
                    f'{_COL_MARCA_ID} int REFERENCES {_REFERENCES_MARCA}, ' \
                    f'{_COL_CATEGORIA_ID} int REFERENCES {_REFERENCES_CATEGORIA}' \
                    f');'
