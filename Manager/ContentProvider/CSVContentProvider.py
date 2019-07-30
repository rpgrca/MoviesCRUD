"""FileContentProvider.py"""

from typing import List, Any
import csv
import os
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.Movie import Movie
from Movie.MoviesFactory import MoviesFactory

class CSVContentProvider(ContentProvider):
    """Content Provider para archivos en formato CSV (en verdad, .tab)"""
    def __init__(self, filenames: List[str]):
        """Constructor, recibe una lista con el nombre del archivo de peliculas y el de categorias"""

        super(CSVContentProvider, self).__init__()
        self.name = "Archivo CSV"
        self.extra_data = [ "movies.csv", "categories.csv" ]
        self.key = CSVContentProvider.KEY()
        self.__delimiter = '\t'
        self.refresh(filenames)

    def refresh(self, filenames: List[str]):
        """Carga los nombres de los archivos"""
        self.__movies_filename = filenames[0] if filenames and filenames[0] else self.extra_data[0]
        self.__categories_filename = filenames[1] if filenames and filenames[1] else self.extra_data[1]

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "csv"

    def load(self):
        """Carga las categorias y las peliculas de los archivos de entrada"""
        if not self.initialized and self.__movies_filename and self.__categories_filename:
            if os.path.isfile(self.__categories_filename):
                with open(self.__categories_filename, "r") as input_file:
                    reader = csv.reader(input_file, delimiter=self.__delimiter)
                    for line in reader:
                        try:
                            if line:
                                identifier, category = line
                                if identifier and identifier != 'id':
                                    self.categories.append(category)
                                else:
                                    pass # El archivo csv tiene header, no procesarlo
                        except:
                            # TODO: Agregar numero de linea
                            raise ValueError("Formato invalido en archivo {}".format(self.__categories_filename))

            if os.path.isfile(self.__movies_filename):
                with open(self.__movies_filename, "r") as input_file:
                    reader = csv.reader(input_file, delimiter=self.__delimiter)
                    for line in reader:
                        try:
                            if line:
                                identifier, title, description, releasedate, director, category = line
                                if identifier and identifier != 'identifier':
                                    movie = MoviesFactory.create1(int(identifier), title, description, releasedate, director, category)
                                    self.movies.append(movie)

                                    if category not in self.categories: # Por si acaso
                                        self.categories.append(category)
                                else:
                                    pass # El archivo csv tiene header, no procesarlo
                        except:
                            # TODO: Agregar numero de linea
                            raise ValueError("Formato invalido en archivo CSV")

            self.initialized = True

    def save(self):
        """Graba los valores en los archivos CSV"""
        if self.__categories_filename and self.__movies_filename and self.initialized:
            categories = [ {'id': i + 1, 'category': x} for i, x in enumerate(self.categories)]

            with open(self.__categories_filename, 'w', newline='') as output_file:
                writer = csv.DictWriter(output_file, delimiter=self.__delimiter, fieldnames=[ 'id', 'category' ])
                writer.writeheader()
                writer.writerows(categories)

            with open(self.__movies_filename, "w", newline='') as output_file:
                writer = csv.DictWriter(output_file, delimiter=self.__delimiter, fieldnames=Movie.getHeaders())
                writer.writeheader()
                for movie in self.movies:
                    writer.writerow(movie.toDictionary())

            self.initialized = False
            self.movies = []
            self.categories = []
