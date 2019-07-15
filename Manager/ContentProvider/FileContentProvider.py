"""FileContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class FileContentProvider(ContentProvider):
    def __init__(self, filename: str):
        super(FileContentProvider, self).__init__()
        self.name = "Archivo de texto"
        self.extra_data = "movies.txt"
        self.key = FileContentProvider.KEY()
        self.__filename = filename if filename else self.extra_data

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "file"

    def load(self):
        # TODO: Cargar items del archivo
        pass

    def save(self):
        # TODO: Grabar items del archivo
        pass
