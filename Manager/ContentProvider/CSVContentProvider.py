#    def _track_rooms_load_previous_day(self, filename):
#        """
#        Auxiliar function, load information from previous day.
#        Currently unused.
#        """
#        _ = timezone('Asia/Tokyo')
#        last = {}
#        with open(filename, "r") as input_file:
#            reader = csv.reader(input_file, delimiter='\t')
#            for room_id, _, date, _, followers, viewers, points, diff in reader:
#                if room_id not in last:
#                    last[room_id] = {
#                        "points": points, "date": date, "viewers": viewers,
#                        "followers": followers, "diff": diff
#                    }
#

"""FileContentProvider.py"""

from typing import List, Any
import csv
import os
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.Movie import Movie
from Movie.MoviesFactory import MoviesFactory

class CSVContentProvider(ContentProvider):
    def __init__(self, filename: str):
        super(CSVContentProvider, self).__init__()
        self.name = "Archivo CSV"
        self.extra_data = "movies.csv"
        self.key = CSVContentProvider.KEY()
        self.__filename = filename if filename else self.extra_data
        self.__delimiter = '\t'

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "csv"

    def load(self):
        if self.__filename and not self.initialized:
            if os.path.isfile(self.__filename):
                with open(self.__filename, "r") as input_file:
                    reader = csv.reader(input_file, delimiter=self.__delimiter)
                    for line in reader:
                        try:
                            if line:
                                identifier, title, description, releasedate, director, category = line
                                if identifier and identifier != 'identifier':
                                    movie = MoviesFactory.create1(int(identifier), title, description, releasedate, director, category)
                                    self.movies.append(movie)

                                    if category not in self.categories:
                                        self.categories.append(category)
                                else:
                                    pass # El archivo csv tiene header
                        except:
                            # TODO: Agregar numero de linea
                            raise ValueError("Formato invalido en archivo CSV")

            self.initialized = True
        

    def save(self):
        if self.__filename and self.initialized:
            with open(self.__filename, "w", newline='') as output_file:
                writer = csv.DictWriter(output_file, delimiter=self.__delimiter, fieldnames=Movie.getHeaders())
                writer.writeheader()
                for movie in self.movies:
                    writer.writerow(movie.toDictionary())

            self.initialized = False
