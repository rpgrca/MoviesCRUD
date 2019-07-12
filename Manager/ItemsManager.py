from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class ItemsManager(object):
    def __init__(self, content_provider: ContentProvider):
        self.__content_provider = content_provider
        self.__items = []
        self.__initialized = False

    def load(self):
        if not self.__initialized and self.__content_provider:
            self.__content_provider.load()
            self.set_items(self.__content_provider.get_items())
            self.__initialized = True

    def get_items(self):
        return self.__items

    def set_items(self, items: List[Any]):
        self.__items = items

    def save(self):
        if self.__content_provider:
            self.__content_provider.save(self.__items)

