from modules.categoria.modelo import Categoria
from modules.marca.modelo import Marca


class Produto:
    def __init__(self, nome, marca: Marca, categoria: Categoria):
        self.nome = nome
        self.marca = marca
        self.categoria = categoria
