"""ZODBContentProvider.py"""

import ZODB
import ZODB.FileStorage
import transaction
from Manager.ContentProvider.ContentProvider import ContentProvider

class ZODBContentProvider(ContentProvider):
    """Manejador de una base de datos ZODB"""

    def __init__(self, filename: str):
        """Constructor"""
        super(ZODBContentProvider, self).__init__()
        self.name = "Base ZODB"
        self.extra_data = "movies.fs"
        self.key = ZODBContentProvider.KEY()
        self.refresh(filename)
        self.__connection = None
        self.__database = None

    def refresh(self, filename: str):
        """Carga el nombre del archivo"""
        self.__filename = filename if filename else self.extra_data
        self.extra_data = self.__filename

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "zodb"

    def load(self):
        """Carga las categorias y las peliculas de la base de datos de ZODB"""
        if not self.initialized:
            try:
                self.__database = ZODB.DB(self.__filename)
                self.__connection = self.__database.open()

                root = self.__connection.root()
                if root and hasattr(root, 'keys'):
                    for key in sorted(root.keys()):
                        if key.startswith('movies'):
                            self.movies.append(root[key])
                        elif key == 'categories':
                            self.categories = root[key]

            except Exception as exception:
                raise ValueError("Hubo un problema leyendo la base de datos: {}".format(exception))

            self.initialized = True

    def save(self):
        """Graba las listas de peliculas y categorias en una base de datos de ZODB"""
        if self.initialized:
            root = self.__connection.root()
            # TODO: Deberia aparear los datos para no borrar siempre todos los datos
            if root and hasattr(root, 'keys'):
                keys = list(root.keys())
                for key in keys:
                    del root[key]

            for movie in self.movies:
                root['movies_{0}'.format(movie.identifier)] = movie

            root['categories'] = self.categories
            transaction.commit()

            self.__connection.close()
            self.__connection = None
            self.__database.close()
            self.__database = None

            self.initialized = False
            self.movies = []
            self.categories = []
