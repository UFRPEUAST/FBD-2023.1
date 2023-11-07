from modules.produto.sql import SQLProduto


class DAOProduto(SQLProduto):
    def __init__(self):
        pass

    def create_table(self):
        return self._CREATE_TABLE
