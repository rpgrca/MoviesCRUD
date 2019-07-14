"""Movie.py"""
import json

class Movie(object):
    def __init__(self, identifier: int = -1, title: str = "", description: str = "", releasedate: str = "", director: str = "", category: str = "", **kwargs):
        """Constructor"""
        if kwargs and kwargs["dictionary"]:
            identifier = kwargs["dictionary"]["identifier"]
            title = kwargs["dictionary"]["title"]
            description = kwargs["dictionary"]["description"]
            releasedate = kwargs["dictionary"]["releasedate"]
            director = kwargs["dictionary"]["director"]
            category = kwargs["dictionary"]["category"]

        self.identifier = identifier
        self.title = title
        self.description = description
        self.releasedate = releasedate
        self.director = director
        self.category = category

    def __get_identifier(self):
        """Retorna el identificador de la pelicula"""
        return self.__identifier

    def __set_identifier(self, value):
        """Asigna el identificador a la pelicula"""
        if value and value > 0:
            self.__identifier = value
        else:
            raise ValueError("El identificador de la pelicula no puede estar vacio ni ser menor a 1")

    def get_title(self):
        """Retorna el titulo de la pelicula"""
        return self.__title

    def set_title(self, value):
        """Asigna el titulo a la pelicula"""
        if value:
            self.__title = value
        else:
            raise ValueError("El titulo de la pelicula no puede estar vacio")

    def get_description(self):
        """Retorna la descripcion de la pelicula"""
        return self.__description

    def set_description(self, value):
        """Asigna la descripcion a la pelicula"""
        if value:
            self.__description = value
        else:
            raise ValueError("La descripcion de la pelicula no puede estar vacio")

    def get_releasedate(self):
        """Retorna la fecha de estreno de la pelicula"""
        return self.__releasedate

    def set_releasedate(self, value):
        """Asigna la fecha de estreno de la pelicula"""
        if value:
            self.__releasedate = value
        else:
            raise ValueError("La fecha de estreno de la pelicula no puede estar vacia")

    def get_director(self):
        """Retorna el director de la pelicula"""
        return self.__director

    def set_director(self, value):
        """Asigna el director a la pelicula"""
        if value:
            self.__director = value
        else:
            raise ValueError("El director de la pelicula no puede estar vacio")

    def get_category(self):
        """Retorna la categoria de la pelicula"""
        return self.__category

    def set_category(self, value):
        """Asigna la categoria a la pelicula"""
        if value:
            self.__category = value
        else:
            raise ValueError("La categoria de la pelicula no puede estar vacia")

    identifier = property(__get_identifier, __set_identifier)
    title = property(get_title, set_title)
    description = property(get_description, set_description)
    releasedate = property(get_releasedate, set_releasedate)
    director = property(get_director, set_director)
    category = property(get_category, set_category)

    def fromDictionary(self, dictionary: dict):
        """Carga los valores del diccionario dado en la estructura interna"""
        self.__dict__ = dictionary

    def toDictionary(self) -> dict:
        """Retorna el diccionario interno para serializar como JSON"""
        return { 'identifier': self.identifier, 'title': self.title, 'description': self.description, 'releasedate': self.releasedate, 'director': self.director, 'category': self.category }
        #return self.__dict__

    def __str__(self):
        """String"""
        return 'Id: {0}, Titulo: {1}, Desc: {2}, Fecha: {3}, Director: {4}, Categoria: {5}'.format(self.__identifier, self.__title, self.__description, self.__releasedate, self.__director, self.category)
