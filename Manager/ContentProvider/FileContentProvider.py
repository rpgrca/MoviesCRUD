from Manager.ContentProvider.ContentProvider import ContentProvider

class FileContentProvider(ContentProvider):
    def __init__(self, filename):
        super(FileContentProvider, self).__init__()
        self.__filename = filename

    def load(self):
        # TODO: Cargar items del archivo
        pass

    def save(self, items):
        # TODO: Grabar items del archivo
        pass
