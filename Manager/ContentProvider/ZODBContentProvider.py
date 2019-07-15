"""ZODBContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class ZODBContentProvider(ContentProvider):
    def __init__(self, connection_string: str):
        """Constructor"""
        super(ZODBContentProvider, self).__init__()
        self.__connection_string = connection_string
        self.name = "Base ZODB"
        self.key = ZODBContentProvider.KEY()

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "zodb"

    def load(self):
        # TODO: Cargar items de la base de datos
        pass

    def save(self):
        # TODO: Grabar items de la base de datos
        pass