class Categoria():
    def __init__(self, descricao, id=None):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return 'Categoria: {}'.format(self.descricao)
