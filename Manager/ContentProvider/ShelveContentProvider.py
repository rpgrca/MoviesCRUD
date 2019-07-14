"""ShelveContentProvider.py"""

from typing import List, Any
import shelve
from Manager.ContentProvider.ContentProvider import ContentProvider

class ShelveContentProvider(ContentProvider):
    def __init__(self, filename: str):
        """Constructor"""
        super(ShelveContentProvider, self).__init__()
        self.__filename = filename
        self.__shelf = None
        self.__initialized = False
        self.name = "Base Shelve"

    def __get_config(self, key: str) -> List[Any]:
        """Retorna la lista grabada en una determinada llave"""
        try:
            value = self.__shelf[key]
        except Exception:
            value = []

        return value

    def load(self):
        """Carga los datos de las peliculas y categorias del shelf"""
        if not self.__initialized:
            self.__shelf =  shelve.open(self.__filename)
            self.movies = self.__get_config("movies")
            self.categories = self.__get_config("categories")
            self.__initialized = True

    def save(self):
        """Graba los datos de las peliculas y categorias en un shelf"""
        if self.__initialized:
            self.__shelf["movies"] = self.movies
            self.__shelf["categories"] = self.categories
            self.__shelf.close()
            self.__initialized = False
            self.__shelf = None
            self.categories = []
            self.movies = []
