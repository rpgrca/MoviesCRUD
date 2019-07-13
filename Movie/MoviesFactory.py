import json
from Movie.Movie import Movie

class MoviesFactory:
    @staticmethod
    def create() -> Movie:
        return Movie()

    @staticmethod
    def create(identifier: int, title: str, description: str, releasedate: str, director: str, category: str) -> Movie:
        movie = Movie()
        movie.identifier = identifier
        movie.title = title
        movie.description = description
        movie.releasedate = releasedate
        movie.director = director
        movie.category = category
        return movie

    @staticmethod
    def create(dictionary: dict) -> Movie:
        movie = Movie()
        movie.fromDictionary(dictionary)
        return movie
