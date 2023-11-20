from modules.marca.modelo import Marca
from modules.marca.sql import SQLMarca
from service.connect import Connect


class DAOMarca(SQLMarca):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def get_by_cnpj(self, cnpj):
        query = self._SELECT_BY_CNPJ
        cursor = self.connection.cursor()
        cursor.execute(query, (cnpj,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Marca(**i) for i in results]
        return results

    def salvar(self, marca: Marca):
        if not isinstance(marca, Marca):
            raise Exception("Tipo inválido")
        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (marca.nome, marca.cnpj))
        self.connection.commit()
        return marca

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Marca(**i) for i in results]
        return results
