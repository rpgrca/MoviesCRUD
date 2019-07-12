class Movie(object):
    def __init__(self, identifier: int, title: str, description: str, releasedate: str, director: str, category: str):
        self.identifier = identifier
        self.title = title
        self.description = description
        self.releasedate = releasedate
        self.director = director
        self.category = category

    def __str__(self):
        return 'Id: {0}, Titulo: {1}, Desc: {2}, Fecha: {3}, Autor: {4}'.format(self.identifier, self.title, self.description, self.releasedate, self.director)
