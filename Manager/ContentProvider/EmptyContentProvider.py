"""EmptyContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class EmptyContentProvider(ContentProvider):
    def __init__(self):
        super(EmptyContentProvider, self).__init__()
        self.name = "Vacio (sin valores)"
        self.initialized = True
        self.key = EmptyContentProvider.KEY()

    @staticmethod
    def KEY() -> str:
        """Retorna la llave de este content provider"""
        return "empty"
