"""SQLiteContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class SQLiteContentProvider(ContentProvider):
    def __init__(self, connection_string: str):
        """Constructor"""
        super(SQLiteContentProvider, self).__init__()
        self.name = "Base SQLite3"
        self.extra_data = "movies.sqlite3"
        self.key = SQLiteContentProvider.KEY()
        self.__connection_string = connection_string if connection_string else self.extra_data

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "sqlite"

    def load(self):
        # TODO: Cargar items de la base de datos
        pass

    def save(self):
        # TODO: Grabar items de la base de datos
        pass
