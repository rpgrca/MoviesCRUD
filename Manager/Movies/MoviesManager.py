"""MoviesManager.py"""

from typing import List
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.Movie import Movie

class MoviesManager(ItemsManager):
    """Manejador de peliculas, mantiene la lista de peliculas actualmente visualizadas por el formulario"""

    def __init__(self, content_provider: ContentProvider):
        """Constructor"""
        super(MoviesManager, self).__init__(content_provider)

    def load(self):
        """Carga los elementos desde el ContentProvider al Manager"""
        if self.content_provider:
            self.content_provider.load()
            self.items = self.content_provider.movies

    def dump(self):
        """Graba los elementos en el Manager en el ContentProvider"""
        if self.content_provider:
            self.content_provider.movies = self.items

    @property
    def movies(self) -> List[Movie]:
        """Retorna la lista actual de peliculas del Manager"""
        return super(MoviesManager, self).items

    # TODO: Ya existe esta funcion en MoviesFactory, consolidar
    def create(self, title: str, description: str, releasedate: str, director: str, category: str) -> Movie:
        """Crea una pelicula con los datos dados"""
        return Movie(self.get_next_identifier(), title, description, releasedate, director, category)

    # TODO: Usualmente se retorna el elemento eliminado
    def remove(self, identifier: int):
        """Borra la pelicula con el identificador dado del Manager"""
        self.items = list(filter(lambda x : x.identifier != identifier, self.items))

    def get_movie(self, identifier: int) -> Movie:
        """Retorna la pelicula cuyo identificador es igual al indicado"""
        result = list(filter(lambda x : x.identifier == identifier, self.items))
        if result and len(result) > 0:
            return result[0]
 
        return None

    def get_next_identifier(self) -> int:
        """Retorna el proximo identificador valido para una pelicula, o 1 si no hay peliculas"""
        if self.items:
            return self.items[-1].identifier + 1
        else:
            return 1
