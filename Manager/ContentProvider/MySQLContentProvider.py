"""MySQLContentProvider.py"""

from typing import List
import mysql.connector #  pip3 install mysql-connector
from mysql.connector import Error, errorcode
from Manager.ContentProvider.ContentProvider import ContentProvider
from Movie.MoviesFactory import MoviesFactory

class MySQLContentProvider(ContentProvider):
    """Manejador de una base de datos MySQL"""

    def __init__(self, connection_string: List[str]):
        """Constructor"""
        super(MySQLContentProvider, self).__init__()
        self.name = "Base MySQL"
        self.extra_data = ["localhost", "root", "1234", "moviesdb"]
        self.key = MySQLContentProvider.KEY()
        self.refresh(connection_string)
        self.__connection = None

    def refresh(self, connection_string: List[str]):
        """Carga el string de conexion a base de datos"""
        self.__host = connection_string[0] if connection_string and connection_string[0] else self.extra_data[0]
        self.__user = connection_string[1] if connection_string and connection_string[1] else self.extra_data[1]
        self.__password = connection_string[2] if connection_string and connection_string[2] else self.extra_data[2]
        self.__database = connection_string[3] if connection_string and connection_string[3] else self.extra_data[3]
        self.extra_data = [self.__host, self.__user, self.__password, self.__database]

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "mysql"

    def load(self):
        """Carga las categorias y las peliculas de la base de datos de MySQL"""
        if not self.__connection and not self.initialized:
            self.categories = {}
            try:
                self.__connection = mysql.connector.connect(user=self.__user, password=self.__password, host=self.__host, database=self.__database)
            except Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    raise ValueError("Error en el usuario o password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    # Si tira esta excepcion tratamos de conectarnos sin base por default y la creamos
                    self.__connection = mysql.connector.connect(user=self.__user, password=self.__password, host=self.__host)
                    cursor = self.__connection.cursor()
                    cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.__database)
                    cursor.execute("USE " + self.__database) # Para no olver a conectarnos
                    cursor.execute('CREATE TABLE IF NOT EXISTS Categories (id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL) ENGINE=InnoDB')
                    cursor.execute('CREATE TABLE IF NOT EXISTS Movies (id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, identifier INT(10) NOT NULL, title VARCHAR(100) NOT NULL, description VARCHAR(1024) NOT NULL, releasedate TEXT NOT NULL, director VARCHAR(100) NOT NULL, category INT(10) NOT NULL, CONSTRAINT category_1 FOREIGN KEY (category) REFERENCES Categories (id) ON DELETE CASCADE) ENGINE=InnoDB')
                    self.__connection.commit()
                    cursor.close()
                else:
                    raise ValueError(err)

            cursor = self.__connection.cursor()
            cursor.execute('SELECT id, name FROM Categories')
            for (_id, name) in cursor:
                self.categories.append(name)

            cursor.close()

            cursor = self.__connection.cursor()
            cursor.execute('SELECT identifier, title, description, releasedate, director, Categories.name FROM Movies, Categories WHERE Movies.category = Categories.id')
            for (identifier, title, description, releasedate, director, category) in cursor:
                self.movies.append(MoviesFactory.create1(int(identifier), title, description, releasedate, director, category))

            cursor.close()
            self.initialized = True

    def save(self):
        """Graba las listas de peliculas y categorias en una base de datos de MySQL"""
        if self.initialized:
            cursor = self.__connection.cursor()
            cursor.execute("DELETE FROM Movies") # TODO: En un mundo ideal, se aparean las listas y no se borra la tabla

            for movie in self.movies:
                cursor.execute("SELECT id FROM Categories WHERE name LIKE %s", (movie.category,))
                result = cursor.fetchone()
                if not result:
                    cursor.execute('INSERT INTO Categories (name) VALUES (%s)', (movie.category,))
                    category_id = cursor.getlastrowid()
                else:
                    category_id = result[0]

                cursor.execute('INSERT INTO Movies (identifier, title, description, releasedate, director, category) VALUES (%s, %s, %s, %s, %s, %s)', (movie.identifier, movie.title, movie.description, movie.releasedate, movie.director, category_id))

            self.__connection.commit()
            self.__connection.close()
            cursor.close()
            self.__connection = None

            self.initialized = False
            self.categories = []
            self.movies = []
