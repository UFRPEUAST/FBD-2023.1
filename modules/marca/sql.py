class SQLMarca:
    _COL_ID = 'id'
    _TABLE_NAME = 'marca'
    _COL_NOME = 'nome'
    _COL_CNPJ = 'cnpj'
    _CAMPOS_OBRIGATORIOS = [_COL_NOME, _COL_CNPJ]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'(id serial primary key, ' \
                    f'{_COL_NOME} varchar(255), ' \
                    f'{_COL_CNPJ} varchar(14));'
    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_CNPJ = f"SELECT * from {_TABLE_NAME} where {_COL_CNPJ} ilike %s"
    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}({_COL_NOME}, {_COL_CNPJ}) values(%s, %s)'
