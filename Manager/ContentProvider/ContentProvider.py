from typing import List, Any
from Movie.Movie import Movie

class ContentProvider(object):
    def __init__(self):
        self.__movies = []
        self.__categories = []

    def load(self):
        pass

    def get_movies(self) -> List[Movie]:
        return self.__movies

    def get_categories(self) -> List[str]:
        return self.__categories

    def set_movies(self, movies: List[Movie]):
        self.__movies = movies

    def set_categories(self, categories: List[str]):
        self.__categories = categories

    def save(self):
        pass
