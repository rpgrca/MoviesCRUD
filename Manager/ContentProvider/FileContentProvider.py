"""FileContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class FileContentProvider(ContentProvider):
    def __init__(self, filename: str):
        super(FileContentProvider, self).__init__()
        self.__filename = filename
        self.name = "Archivo de texto"
        self.key = FileContentProvider.KEY()

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
