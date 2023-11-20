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

    def init_database(self, version='v1'):
        if version == 'v1':
            self.create_tables()
        if version == 'v2':
            self.update_database()
    def update_database(self):
        pass
# produto - nome, marca, categoria
# item_produto = cod_barra, numero_lote, data_entrada, data_validade, quantidadem quantidade_disponivel
# preço_compra, preco_venda, produto

#Promocao - Nome, dia - porcentagem

#Como a relação de promoção com o item é e N para N
#sera criado uma tabela auxiliar, onde

# PromocaoItem - id, promocao_id, item_id, total_disponivel, total_vendido, status
#Onde o status será aberto ou fechado






# Select p.nome, p.marca_id from produto as p
#
#
#
# select p.nome as produto, m.nome as marca
# from produto as p, marca as m
# where p.marca_id=m.id;
#
# select m.nome as marca
# from produto as p
#     RiGHT Join marca as m
#     on m.id=p.marca_id where p is Null
#
# select m.nome
# from marca m
# where m.id not in (select
#     DISTINCT p.marca_id
# from produto p)
