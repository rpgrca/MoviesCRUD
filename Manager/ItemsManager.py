"""ItemsManager.py"""
from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class ItemsManager(object):
    def __init__(self, content_provider: ContentProvider):
        """Constructor"""
        self.__content_provider = content_provider
        self.__items = []

    def load(self):
        """Carga la lista de items desde el Content Provider"""
        pass

    def get_items(self):
        """Retorna los items cargados en el Manager"""
        # TODO: Tal vez deberia llamar a self.load()
        return self.__items

    def set_items(self, items: List[Any]):
        """Reemplaza los items del Manager con una nueva lista de elementos"""
        self.__items = items

    def get_content_provider(self):
        """Retorna el Content Provider interno"""
        return self.__content_provider

    def dump(self):
        """Inserta los elementos de la lista del Manager dentro del Content Provider"""
        self.__items = []
