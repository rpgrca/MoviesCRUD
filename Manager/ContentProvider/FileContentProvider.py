"""FileContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class FileContentProvider(ContentProvider):
    """Manejador de archivos de texto con un formato determinado"""

    def __init__(self, filename: str):
        """Constructor"""
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
        """Carga las categorias y las peliculas del archivo de entrada"""
        # TODO: Cargar items del archivo usando RegEx
        pass

    def save(self):
        """Graba las listas de peliculas y categorias en un de texto"""
        # TODO: Grabar items del archivo
        pass
