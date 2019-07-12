from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class ShelveContentProvider(ContentProvider):
    def __init__(self, database: str):
        super(ShelveContentProvider, self).__init__()
        self.__database = database

    def load(self):
        # TODO: Cargar items de la base
        pass

    def get_items(self) -> List[Any]:
        return self.__items

    def save(self, items: List[Any]):
        # TODO: Cargar items de la base
        pass
