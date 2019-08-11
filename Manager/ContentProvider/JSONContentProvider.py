"""JSONContentProvider.py"""

import os
import json
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.MoviesFactory import MoviesFactory

class JSONContentProvider(ContentProvider):
    """Manejador de archivos en formato JSON"""

    def __init__(self, filename: str):
        """Constructor"""
        super(JSONContentProvider, self).__init__()
        self.name = "Archivo JSON"
        self.extra_data = "movies.json"
        self.key = JSONContentProvider.KEY()
        self.refresh(filename)

    def refresh(self, filename: str):
        """Carga el nombre del archivo"""
        self.__filename = filename if filename else self.extra_data
        self.extra_data = self.__filename

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "json"

    def load(self):
        """Carga las listas de peliculas y categorias desde un archivo JSON"""
        if not self.initialized:
            try:
                respjson = self.__load_json(self.__filename)
                if respjson is not None:
                    if respjson.get("movies"):
                        self.movies = [MoviesFactory.create(x) for x in respjson["movies"]]

                    if respjson.get("categories"):
                        self.categories = respjson["categories"]
                self.initialized = True

            except Exception as exception:
                raise ValueError("Hubo un problema leyendo del archivo {}: {}".format(self.__filename, exception))

    def save(self):
        """Graba las listas de peliculas y categorias en un archivo JSON"""
        if self.initialized:
            dictionary = {}
            dictionary["movies"] = [x.to_dictionary() for x in self.movies] # Esto sirve solo para clases simples como las mias
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
        except Exception as exception:
            raise ValueError("Hubo un problema leyendo el archivo {}: {}".format(filename, exception))

        return filejson

    def __save_json(self, filename: str, dictionary: {}):
        """Seriealiza el diccionario dado a un archivo con formato JSON"""
        try:
            text = json.dumps(dictionary, indent=4, sort_keys=True)
            with open(filename, 'w') as outputfile:
                outputfile.write(text)
        except Exception as ex:
            print(ex)
