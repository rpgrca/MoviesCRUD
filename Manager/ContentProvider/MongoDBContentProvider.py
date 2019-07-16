"""MongoDBContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class MongoDBContentProvider(ContentProvider):
    """Manejador de una base de datos MongoDB"""

    def __init__(self, connection_string: str):
        """Constructor"""
        super(MongoDBContentProvider, self).__init__()
        self.name = "Base MongoDB"
        self.extra_data = "mongodb://127.0.0.1:8889/moviesdb"
        self.key = MongoDBContentProvider.KEY()
        self.__connection_string = connection_string if connection_string else self.extra_data

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "mongodb"

    def load(self):
        """Carga las categorias y las peliculas de la base de datos de MongoDB"""
        # TODO: Cargar items de la base de datos
        pass

    def save(self):
        """Graba las listas de peliculas y categorias en la base de datos de MongoDB"""
        # TODO: Grabar items de la base de datos
        pass
