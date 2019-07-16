"""SQLiteContentProvider.py"""

from typing import List, Any
import sqlite3
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.MoviesFactory import MoviesFactory

class SQLiteContentProvider(ContentProvider):
    """Manejador de una base de datos SQLite"""

    MOVIES_TABLE = "movies"
    CATEGORIES_TABLE = "categories"

    def __init__(self, filename: str):
        """Constructor"""
        super(SQLiteContentProvider, self).__init__()
        self.name = "Base SQLite3"
        self.extra_data = "movies.sqlite3"
        self.key = SQLiteContentProvider.KEY()
        self.__filename = filename if filename else self.extra_data
        self.__connection = None

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "sqlite"

    def load(self):
        """Carga las categorias y las peliculas de la base de datos de SQLite"""

        if not self.__connection:
            categories = {}
            self.__connection = sqlite3.connect(self.__filename)
            self.__connection.execute('CREATE TABLE IF NOT EXISTS Categories (id INTEGER PRIMARY KEY, name varchar(100) NOT NULL)')
            self.__connection.execute('CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, title varchar(100) NOT NULL, description varchar(1024) NOT NULL, releasedate TEXT NOT NULL, director varchar(100) NOT NULL, category INTEGER NOT NULL, FOREIGN KEY(category) REFERENCES categories(id))')
            self.__connection.commit()

            cursor = self.__connection.cursor()
            for row in cursor.execute('SELECT * FROM Categories'):
                categories[row[0]] = row[1]

            cursor.close()

            cursor = self.__connection.cursor()
            for row in cursor.execute('SELECT * FROM Movies'):
                self.movies.append(MoviesFactory.create1(int(row[0]), row[1], row[2], row[3], row[4], categories[row[5]]))

            self.categories = list(categories.values())
            cursor.close()

    def save(self):
        """Graba las listas de peliculas y categorias en una base de datos de SQLite"""
        if self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute("DELETE FROM Movies")

                for movie in self.movies:
                    cursor.execute("SELECT id FROM Categories WHERE name LIKE '{}'".format(movie.category))
                    result = cursor.fetchone()
                    if not result:
                        cursor.execute("INSERT INTO Categories (name) VALUES ('{}')".format(movie.category))
                        category_id = cursor.lastrowid
                    else:
                        category_id = result[0]

                    cursor.execute("INSERT INTO Movies (title, description, releasedate, director, category) VALUES ('{}', '{}', '{}', '{}', {})".format(movie.title, movie.description, movie.releasedate, movie.director, category_id))

                self.__connection.commit()
                cursor.close()
            except sqlite3.IntegrityError:
                print("El ID ya existe en la base de datos")

            self.__connection.close()
