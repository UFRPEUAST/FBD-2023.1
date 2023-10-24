def insert_item(cod_barra, numero_lote, data_entrada,
                data_validade, quantidade, preco_compra, preco_venda,
                produto_id
                ):
    quantidade_disponivel = quantidade

    values = ("'{}','{}','{}','{}','{}','{}','{}','{}','{}'"
              .format(cod_barra,
                      numero_lote, data_entrada,
                      data_validade, quantidade,
                      quantidade_disponivel, preco_compra,
                      preco_venda, produto_id))

    insert_item = ('''insert into item_produto(codigo_barras,
                   numero_lote,
                   data_entrada,
                   data_validade,
                   quantidade,
                   quantidade_disponivel,
                   preco_compra,
                   preco_venda,
                   produto_id) values({});'''.format(values))
    return insert_item
