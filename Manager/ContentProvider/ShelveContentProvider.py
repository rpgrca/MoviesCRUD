from Manager.ContentProvider.ContentProvider import ContentProvider

class ShelveContentProvider(ContentProvider):
    def __init__(self, database):
        super(ShelveContentProvider, self).__init__()
        self.__database = database

    def load(self):
        # TODO: Cargar items de la base
        pass

    def get_items(self):
        return self.__items

    def save(self, items):
        # TODO: Cargar items de la base
        pass
