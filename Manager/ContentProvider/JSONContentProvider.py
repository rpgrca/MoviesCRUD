"""ShelveContentProvider.py"""

from typing import List, Any
import os
import json
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.MoviesFactory import MoviesFactory
from Movie.Movie import Movie

class JSONContentProvider(ContentProvider):
    def __init__(self, filename: str):
        """Constructor"""
        super(JSONContentProvider, self).__init__()
        self.__filename = filename
        self.name = "Archivo JSON"

    def load(self):
        """Carga las listas de peliculas y categorias desde un archivo JSON"""
        if not self.initialized:
            respjson = self.__load_json(self.__filename)
            if respjson is not None:
                if respjson.get("movies"):
                    self.movies = [MoviesFactory.create(x) for x in respjson["movies"]]

                if respjson.get("categories"):
                    self.categories = respjson["categories"]
            self.initialized = True

    def save(self):
        """Graba las listas de peliculas y categorias en un archivo JSON"""
        if self.initialized:
            # Esto sirve solo para clases simples como las mias
            dictionary = {}
            dictionary["movies"] = [x.toDictionary() for x in self.movies]
            dictionary["categories"] = self.categories
            self.__save_json(self.__filename, dictionary)
            self.initialized = False
            self.categories = []
            self.movies = []

    def __load_json(self, filename: str) -> object:
        """Carga los datos del archivo y devuelve el objeto JSON"""
        filejson = None
        try:
            if os.path.isfile(filename):
                with open(filename, 'r') as inputfile:
                    filejson = json.load(inputfile)
        except Exception as ex:
            print(ex)

        return filejson

    def __save_json(self, filename: str, dictionary: {}):
        """Seriealiza el diccionario dado a un archivo con formato JSON"""
        try:
            text = json.dumps(dictionary, indent=4, sort_keys=True)
            with open(filename, 'w') as outputfile:
                outputfile.write(text)
        except Exception as ex:
            print(ex)