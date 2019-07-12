from Manager.ContentProvider.ContentProvider import ContentProvider

class CategoriesContentProvider(ContentProvider):
    def __init__(self):
        super(CategoriesContentProvider, self).__init__()

    def load(self):
        self.set_items(["Accion", "Comedia", "Suspenso", "Terror"])
        pass
