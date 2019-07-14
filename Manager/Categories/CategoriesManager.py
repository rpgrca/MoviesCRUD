"""CategoriesManager.py"""

from typing import List, Any
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider

class CategoriesManager(ItemsManager):
    def __init__(self, content_provider: ContentProvider):
        """Constructor"""
        super(CategoriesManager, self).__init__(content_provider)

    def load(self):
        """Carga los elementos desde el ContentProvider al Manager"""
        if self.get_content_provider():
            self.get_content_provider().load()
            self.set_items(self.get_content_provider().categories)

    def dump(self):
        """Graba los elementos en el Manager en el ContentProvider"""
        if self.get_content_provider():
            self.get_content_provider().categories = self.get_items()

    @property
    def categories(self) -> List[str]:
        """Retorna la lista actual de categorias del Manager"""
        return super(CategoriesManager, self).get_items()

    def create(self, category: str) -> str:
        if category not in self.categories:
            self.categories.append(category)

        return category

    def get_category_index(self, category: str) -> int:
        index = self.categories.index(category)
        if index >= len(self.categories):
            index = -1

        return index
