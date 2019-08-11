"""EmptyContentProvider.py"""

from Manager.ContentProvider.ContentProvider import ContentProvider

class EmptyContentProvider(ContentProvider):
    """Manejador vacio, no carga ni graba en ningun soporte pero permite utilizar el programa"""
    def __init__(self):
        """Constructor"""
        super(EmptyContentProvider, self).__init__()
        self.name = "Vacio (sin valores)"
        self.initialized = True
        self.key = EmptyContentProvider.KEY()

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "empty"

    def refresh(self):
        """Carga los nombres de los archivos"""
        pass
