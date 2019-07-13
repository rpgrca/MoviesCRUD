"""ShelveContentProvider.py"""

from typing import List, Any
import shelve
from Manager.ContentProvider.ContentProvider import ContentProvider

class ShelveContentProvider(ContentProvider):
    def __init__(self, filename: str):
        """Constructor"""
        super(ShelveContentProvider, self).__init__()
        self.__filename = filename
        self.__shelf = None
        self.__initialized = False

    def __get_config(self, key):
        try:
            value = self.__shelf[key]
        except Exception:
            value = []

        return value

    def load(self):
        if not self.__initialized:
            self.__shelf =  shelve.open(self.__filename)
            self.set_movies(self.__get_config("movies"))
            self.set_categories(self.__get_config("categories"))
            self.__initialized = True

    def get_items(self) -> List[Any]:
        return self.__items

    def save(self):
        if self.__initialized:
            self.__shelf["movies"] = self.get_movies()
            self.__shelf["categories"] = self.get_categories()
            self.__shelf.close()
            self.__initialized = False
            self.__shelf = None
            self.set_categories([])
            self.set_movies([])
