"""ItemsManager.py"""
from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class ItemsManager(object):
    """Base para todos los manejadores del programa"""

    def __init__(self, content_provider: ContentProvider):
        """Constructor"""
        self.__content_provider = content_provider
        self.__items = []

    def load(self):
        """Carga la lista de items desde el Content Provider"""
        pass

    def __get_items(self) -> List[Any]:
        """Retorna los items cargados en el Manager"""
        return self.__items

    def __set_items(self, items: List[Any]):
        """Reemplaza los items del Manager con una nueva lista de elementos"""
        self.__items = items

    items = property(__get_items, __set_items)

    @property
    def content_provider(self):
        """Retorna el Content Provider interno"""
        return self.__content_provider

    def dump(self):
        """Inserta los elementos de la lista del Manager dentro del Content Provider"""
        self.__items = []
