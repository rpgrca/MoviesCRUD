"""MoviesManager.py"""

from typing import List
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.Movie import Movie

class MoviesManager(ItemsManager):
    def __init__(self, content_provider: ContentProvider):
        """Constructor"""
        super(MoviesManager, self).__init__(content_provider)

    def load(self):
        """Carga los elementos desde el ContentProvider al Manager"""
        if self.get_content_provider():
            self.get_content_provider().load()
            self.set_items(self.get_content_provider().get_movies())

    def dump(self):
        """Graba los elementos en el Manager en el ContentProvider"""
        if self.get_content_provider():
            self.get_content_provider().set_movies(self.get_items())

    def get_movies(self) -> List[Movie]:
        """Retorna la lista actual de peliculas del Manager"""
        return super(MoviesManager, self).get_items()

    def create(self, title: str, description: str, releasedate: str, director: str, category: str) -> Movie:
        """Crea una pelicula con los datos dados"""
        return Movie(self.get_next_identifier(), title, description, releasedate, director, category)

    def remove(self, identifier: int):
        """Borra la pelicula con el identificador dado del Manager"""
        self.set_items(list(filter(lambda x : x.identifier != identifier, self.get_items())))

    def get_movie(self, identifier: str) -> Movie:
        """Retorna la pelicula cuyo identificador ha sido dado"""
        result = list(filter(lambda x : x.identifier == identifier, self.get_items()))
        if result and len(result) > 0:
            return result[0]
 
        return None

    def get_next_identifier(self) -> int:
        """Retorna el proximo identificador valido para una pelicula"""
        if self.get_items():
            return self.get_items()[-1].identifier + 1
        else:
            return 1
