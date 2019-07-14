"""MongoDBContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class MongoDBContentProvider(ContentProvider):
    def __init__(self, connection_string: str):
        super(MongoDBContentProvider, self).__init__()
        self.__connection_string = connection_string
        self.name = "Base MongoDB"
        self.key = MongoDBContentProvider.KEY()

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
