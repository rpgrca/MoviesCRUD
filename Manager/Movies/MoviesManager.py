from typing import List
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.Movie import Movie

class MoviesManager(ItemsManager):
    def __init__(self, content_provider : ContentProvider):
        super(MoviesManager, self).__init__(content_provider)

    def create(self, title: str, description: str, releasedate: str, director: str, category: str) -> Movie:
        return Movie(self.get_next_identifier(), title, description, releasedate, director, category)

    def remove(self, identifier: int):
        self.set_items(list(filter(lambda x : x.identifier != identifier, self.get_items())))

    def get_movies(self) -> List[Movie]:
        return super(MoviesManager, self).get_items()

    def get_movie(self, identifier: str) -> Movie:
        result = list(filter(lambda x : x.identifier == identifier, self.get_items()))
        if result and len(result) > 0:
            return result[0]
 
        return None

    def get_next_identifier(self) -> int:
        if self.get_items():
            return self.get_items()[-1].identifier + 1
        else:
            return 1

