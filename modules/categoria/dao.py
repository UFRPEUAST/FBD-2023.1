from modules.categoria.modelo import Categoria
from modules.categoria.sql import SQLCategoria
from service.connect import Connect


class DAOCategoria(SQLCategoria):
    def __init__(self, ):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, categoria: Categoria):
        if not isinstance(categoria, Categoria):
            raise Exception("Tipo inválido")
        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (categoria.descricao,))
        self.connection.commit()
        return categoria


    def get_by_description(self, descricao):
        query = self._SELECT_BY_DESCRICAO
        cursor = self.connection.cursor()
        cursor.execute(query, (descricao,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Categoria(**i) for i in results]
        return results


    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Categoria(**i) for i in results]
        return results