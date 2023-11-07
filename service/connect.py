import psycopg2

class Connect:

    def __init__(self):
        config = dict(
            dbname="estoque_fbd_2023_1",
            user="postgres", password="postgres",
            host="localhost", port="5432"
        )
        self._connection = psycopg2.connect(**config)

    def create_tables(self):
        from modules.categoria.dao import DAOCategoria
        from modules.marca.dao import DAOMarca
        from modules.produto.dao import DAOProduto
        cursor = self._connection.cursor()
        cursor.execute(DAOMarca().create_table())
        cursor.execute(DAOCategoria().create_table())
        cursor.execute(DAOProduto().create_table())
        self._connection.commit()
        cursor.close()

    def get_instance(self):
        return self._connection


# produto - nome, marca, categoria
# item_produto = cod_barra, numero_lote, data_entrada, data_validade, quantidadem quantidade_disponivel
# preço_compra, preco_venda, produto
