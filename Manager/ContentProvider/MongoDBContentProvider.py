"""MongoDBContentProvider.py"""

from typing import List, Any
import pymongo # pip3 install pymongo
from pymongo import MongoClient
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.MoviesFactory import MoviesFactory
from Movie.Movie import Movie

class MongoDBContentProvider(ContentProvider):
    """Manejador de una base de datos MongoDB"""

    def __init__(self, connection_string: str):
        """Constructor"""
        super(MongoDBContentProvider, self).__init__()
        self.name = "Base MongoDB"
        self.extra_data = "mongodb://127.0.0.1:27017/moviesdb"
        self.key = MongoDBContentProvider.KEY()
        self.refresh(connection_string)
        self.__client = None

    def refresh(self, connection_string: str):
        """Carga el string de conexion a base de datos"""
        self.__connection_string = connection_string if connection_string else self.extra_data
        self.extra_data = self.__connection_string

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "mongodb"

    def load(self):
        """Carga las categorias y las peliculas de la base de datos de MongoDB"""
        if not self.initialized:
            self.__client = MongoClient(self.__connection_string, serverSelectionTimeoutMS=5000)
            if self.__client:
                db = self.__client['MoviesCRUD']
                for movie in db.movies.find():
                    self.movies.append(MoviesFactory.create1(movie['identifier'], movie['title'], movie['description'], movie['releasedate'], movie['director'], movie['category']))

                for category in db.categories.find():
                    self.categories.append(category['category'])

                self.initialized = True
            else:
                raise ValueError("No se pudo conectar a la base de datos")

    def save(self):
        """Graba las listas de peliculas y categorias en la base de datos de MongoDB"""
        if self.initialized:
            db = self.__client['MoviesCRUD']
            db.movies.delete_many({}) # TODO: Armar una lista de elementos borrados para no borrar toda la base

            for movie in self.movies:
                if db.movies.find_one_and_update({'identifier': movie.identifier}, {'$set': movie.toDictionary()}) is None:
                    db.movies.insert(movie.toDictionary())

            # Las categorias nunca se borran
            for category in self.categories:
                result = db.categories.find_one({'category': category})
                if result is None:
                    db.categories.insert({'category': category})

            self.__client = None

            self.initialized = False
            self.movies = []
            self.categories = []
