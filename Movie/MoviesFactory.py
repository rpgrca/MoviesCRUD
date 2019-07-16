from Movie.Movie import Movie

class MoviesFactory:
    """Fabrica para crear las clases de peliculas necesarias. Podria ser reemplazada por un metodo de clase en Movie"""
    @staticmethod
    def create1(identifier: int, title: str, description: str, releasedate: str, director: str, category: str) -> Movie:
        """Crea una pelicula con los atributos indicados"""
        return Movie(identifier, title, description, releasedate, director, category)

    @staticmethod
    def create(dictionary: dict) -> Movie:
        """Crea una pelicula con los atributos indicados en el diccionario"""
        return Movie(dictionary=dictionary)
