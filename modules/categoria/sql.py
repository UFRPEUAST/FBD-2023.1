class SQLCategoria:
    _COL_ID = 'id'
    _TABLE_NAME = 'categoria'
    _COL_DESCRICAO = 'descricao'
    _CAMPOS_OBRIGATORIOS = [_COL_DESCRICAO]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'(id serial primary key, ' \
                    f'{_COL_DESCRICAO} varchar(255));'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}({_COL_DESCRICAO}) values(%s)'
    _SELECT_BY_DESCRICAO = f"SELECT * from {_TABLE_NAME} where {_COL_DESCRICAO} ilike %s"
    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"