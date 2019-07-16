"""MySQLContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class MySQLContentProvider(ContentProvider):
    """Manejador de una base de datos MySQL"""

    def __init__(self, connection_string: str):
        """Constructor"""
        super(MySQLContentProvider, self).__init__()
        self.name = "Base MySQL"
        self.extra_data = "host=localhost,user=root,passwd=1234,db=moviesdb"
        self.key = MySQLContentProvider.KEY()
        self.__connection_string = connection_string if connection_string else self.extra_data

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "mysql"

    def load(self):
        """Carga las categorias y las peliculas de la base de datos de MySQL"""
        # TODO: Cargar items de la base de datos
        pass

    def save(self):
        """Graba las listas de peliculas y categorias en una base de datos de MySQL"""
        # TODO: Grabar items de la base de datos
        pass
