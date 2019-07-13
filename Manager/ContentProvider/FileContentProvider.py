"""FileContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class FileContentProvider(ContentProvider):
    def __init__(self, filename: str):
        super(FileContentProvider, self).__init__()
        self.__filename = filename

    def get_name(self) -> str:
        return "Archivo de texto"

    def load(self):
        # TODO: Cargar items del archivo
        pass

    def save(self):
        # TODO: Grabar items del archivo
        pass
