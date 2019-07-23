"""MySQLContentProvider.py"""

from typing import List, Any
import mysql.connector #  pip3 install mysql-connector
from Manager.ContentProvider.ContentProvider import ContentProvider

class MySQLContentProvider(ContentProvider):
    """Manejador de una base de datos MySQL"""

    def __init__(self, connection_string: List[str]):
        """Constructor"""
        super(MySQLContentProvider, self).__init__()
        self.name = "Base MySQL"
        self.extra_data = ["localhost", "root", "1234", "moviesdb"] #"host=localhost,user=root,passwd=1234,db=moviesdb"
        self.key = MySQLContentProvider.KEY()
        self.__host = connection_string[0] if connection_string and connection_string[0] else self.extra_data[0]
        self.__user = connection_string[1] if connection_string and connection_string[1] else self.extra_data[1]
        self.__password = connection_string[2] if connection_string and connection_string[2] else self.extra_data[2]
        self.__database = connection_string[3] if connection_string and connection_string[3] else self.extra_data[3]
        self.__connection = None

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "mysql"

    def load(self):
        """Carga las categorias y las peliculas de la base de datos de MySQL"""
        if not self.__connection:
            categories = {}
            try:
                self.__connection = mysql.connector.connect(user=self.__user, password=self.__password, host=self.__host, database=self.__database)
            except mysql.connector.Error as err:
                if err.errno == mysql.errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Error en el usuario y/o password")
                elif err.errno == mysql.errorcode.ER_BAD_DB_ERROR:
                    print("La base de datos no existe")
                else:
                    print(err)
            
            cursor = self.__connection.cursor()
            #cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.__database)
            #cursor.execute("USE " + self.__database) # Para no olver a conectarnos
            #cursor.execute('CREATE TABLE IF NOT EXISTS Categories (id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL) ENGINE=InnoDB')
            #cursor.execute('CREATE TABLE IF NOT EXISTS Movies (id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(100) NOT NULL, description VARCHAR(1024) NOT NULL, releasedate TEXT NOT NULL, director VARCHAR(100) NOT NULL, category INT(10) NOT NULL, CONSTRAINT category_1 FOREIGN KEY (category) REFERENCES Categories (id) ON DELETE CASCADE) ENGINE=InnoDB')

            cursor.execute('SELECT id, name FROM Categories')
            for (id, name) in cursor:
                categories[id] = name

            self.categories = list(categories.values())

            cursor.execute('SELECT Movies.id, title, description, releasedate, director, Categories.name FROM Movies, Categories WHERE Movies.category = Categories.id')
            rows = cursor.fetchall()
            for (id, title, description, releasedate, director, category) in rows:
                self.movies.append(MoviesFactory.create1(int(id), title, description, releasedate, director, categories[category]))

            cursor.close()

    def save(self):
        """Graba las listas de peliculas y categorias en una base de datos de MySQL"""
        if self.__connection:
            cursor = self.__connection.cursor()
            cursor.execute("DELETE FROM Movies")

            for movie in self.movies:
                cursor.execute("SELECT id FROM Categories WHERE name LIKE '%s'", (movie.category))
                result = cursor.fetchone()
                if not result:
                    cursor.execute('INSERT INTO Categories (name) VALUES (%s)', (movie.category,))
                    category_id = cursor.lastrowid
                else:
                    category_id = result[0]

                cursor.execute('INSERT INTO Movies (title, description, releasedate, director, category) VALUES (%s, %s, %s, %s, %s)', (movie.title, movie.description, movie.releasedate, movie.director, category_id))

            self.__connection.commit()
            cursor.close()
