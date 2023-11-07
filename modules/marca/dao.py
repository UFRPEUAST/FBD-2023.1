from modules.marca.sql import SQLMarca


class DAOMarca(SQLMarca):
    def __init__(self):
        pass

    def create_table(self):
        return self._CREATE_TABLE
