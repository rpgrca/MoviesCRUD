"""MongoDBContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class MongoDBContentProvider(ContentProvider):
    def __init__(self, connection_string: str):
        super(MongoDBContentProvider, self).__init__()
        self.name = "Base MongoDB"
        self.extra_data = "mongodb://127.0.0.1:8889/movies"
        self.key = MongoDBContentProvider.KEY()
        self.__connection_string = connection_string if connection_string else self.extra_data

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "mongodb"

    def load(self):
        # TODO: Cargar items de la base de datos
        pass

    def save(self):
        # TODO: Grabar items de la base de datos
        pass
