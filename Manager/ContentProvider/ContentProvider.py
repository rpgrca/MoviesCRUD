from typing import List, Any
from Movie.Movie import Movie

class ContentProvider(object):
    def __init__(self):
        """Constructor"""
        self.__movies = []
        self.__categories = []

    def get_name(self):
        """Retorna el nombre del Content Provider"""
        pass

    def load(self):
        """Carga los valores desde el origen a las listas internas"""
        pass

    def get_movies(self) -> List[Movie]:
        """Retorna la lista de peliculas leidas"""
        return self.__movies

    def get_categories(self) -> List[str]:
        """Retorna la lista de categorias leidas"""
        return self.__categories

    def set_movies(self, movies: List[Movie]):
        """Reemplaza la lista de peliculas interna por otra"""
        self.__movies = movies

    def set_categories(self, categories: List[str]):
        """Reemplaza la lista de categorias interna por otra"""
        self.__categories = categories

    def save(self):
        """Graba los valores al origen"""
        pass
