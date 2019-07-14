import json
from Movie.Movie import Movie

class MoviesFactory:
#    @staticmethod
#    def create() -> Movie:
#        return Movie()

    @staticmethod
    def create(identifier: int, title: str, description: str, releasedate: str, director: str, category: str) -> Movie:
        return Movie(identifier, title, description, releasedate, director, category)

    @staticmethod
    def create(dictionary: dict) -> Movie:
        movie = Movie(dictionary=dictionary)
        #movie.fromDictionary(dictionary)
        return movie
