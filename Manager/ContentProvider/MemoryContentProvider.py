"""MemoryContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.Movie import Movie

class MemoryContentProvider(ContentProvider):
    """Manejador de datos en memoria, a diferencia de EmptyContentProvider ofrece algunos datos por defecto"""

    def __init__(self):
        """Constructor"""
        super(MemoryContentProvider, self).__init__()
        self.__categories = [ "Accion", "Comedia", "Suspenso", "Terror" ]
        self.__movies = [ Movie(1, "The Terminator", "American science fiction film", '1984-10-26', "James Cameron", "Accion"),
                          Movie(2, "RoboCop", "Crime/Sci-fi", '1987-09-17', "Paul Verhoeven", "Accion"),
                          Movie(3, "A Nightmare on Elm Street", "Mystery/Slasher", '1984-11-09', "Wes Craven", "Suspenso"),
                          Movie(4, "Friday the 13th", "Slasher film", '1980-05-09', "Sean S. Cunningham", "Terror"),
                          Movie(5, "Back to the Future", "Fantasy/Sci-fi", '1985-12-26', "Robert Zemeckis", "Comedia") ]
        self.name = "Memoria Volatil"
        self.key = MemoryContentProvider.KEY()

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "memory"

    def load(self):
        """Carga las peliculas y categorias por defecto"""
        self.movies = self.__movies
        self.categories = self.__categories
        self.initialized = True
