class SQLMarca:
    _COL_ID = 'id'
    _TABLE_NAME = 'marca'
    _COL_NOME = 'nome'
    _COL_CNPJ = 'cnpj'
    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                   f'(id serial primary key, ' \
                   f'{_COL_NOME} varchar(255), ' \
                   f'{_COL_CNPJ} varchar(14));'
