from typing import List, Any

class ContentProvider(object):
    def __init__(self):
        self.__items = []

    def load(self):
        pass

    def get_items(self) -> List[Any]:
        return self.__items

    def set_items(self, items: List[Any]):
        self.__items = items

    def save(self, items: List[Any]):
        self.__items = items

