from typing import List, Any
from Movie.Movie import Movie

class ContentProvider(object):
    def __init__(self):
        """Constructor"""
        self.__movies = []
        self.__categories = []
        self.__name = None
        self.__key = None
        self.__initialized = False

    def __get_key(self) -> str:
        """Retorna la llave de la fabrica del Content Provider"""
        return self.__key

    def __set_key(self, value: str):
        """Asigna la llave de la fabrica al Content Provider"""
        if value:
            self.__key = value
        else:
            raise ValueError("La llave del Content Provider no puede estar vacia")

    def __get_name(self) -> str:
        """Retorna el nombre del Content Provider"""
        return self.__name

    def __set_name(self, value: str):
        """Asigna el nombre al Content Provider"""
        if value:
            self.__name = value
        else:
            raise ValueError("El nombre del Content Provider no puede estar vacio")

    def __get_movies(self) -> List[Movie]:
        """Retorna la lista de peliculas leidas"""
        return self.__movies

    def __set_movies(self, movies: List[Movie]):
        """Reemplaza la lista de peliculas interna por otra"""
        self.__movies = movies

    def __get_categories(self) -> List[str]:
        """Retorna la lista de categorias leidas"""
        return self.__categories

    def __set_categories(self, categories: List[str]):
        """Reemplaza la lista de categorias interna por otra"""
        self.__categories = categories

    def __get_initialized(self) -> bool:
        """Retorna si el content provider esta inicializado"""
        return self.__initialized

    def __set_initialized(self, value: bool):
        """Asigna si el Content Provider esta inicializado"""
        self.__initialized = value

    name = property(__get_name, __set_name)
    key = property(__get_key, __set_key)
    initialized = property(__get_initialized, __set_initialized)
    movies = property(__get_movies, __set_movies)
    categories = property(__get_categories, __set_categories)

    def load(self):
        """Carga los valores desde el origen a las listas internas"""
        pass

    def save(self):
        """Graba los valores al origen"""
        pass
