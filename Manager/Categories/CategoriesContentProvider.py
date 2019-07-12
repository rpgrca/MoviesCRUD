from Manager.ContentProvider.ContentProvider import ContentProvider

class CategoriesMemoryContentProvider(ContentProvider):
    def __init__(self):
        super(CategoriesMemoryContentProvider, self).__init__()

    def load(self):
        self.set_items(["Accion", "Comedia", "Suspenso", "Terror"])
        pass
