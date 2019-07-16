"""CategoriesManager.py"""

from typing import List, Any
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider

class CategoriesManager(ItemsManager):
    """Manejador de categorias, mantiene la lista de categorias existentes en memoria"""

    def __init__(self, content_provider: ContentProvider):
        """Constructor"""
        super(CategoriesManager, self).__init__(content_provider)

    def load(self):
        """Carga los elementos desde el ContentProvider al Manager"""
        if self.content_provider:
            self.content_provider.load()
            self.items = self.content_provider.categories

    def dump(self):
        """Graba los elementos en el Manager en el ContentProvider"""
        if self.content_provider:
            self.content_provider.categories = self.items

    @property
    def categories(self) -> List[str]:
        """Retorna la lista actual de categorias del Manager"""
        return super(CategoriesManager, self).items

    def create(self, category: str) -> str:
        """Crea una nueva categoria si no existe dentro de la lista"""
        if category not in self.categories:
            self.categories.append(category)

        return category

    def get_category_index(self, category: str) -> int:
        """Retorna el indice de la categoria indicada en la lista"""
        index = self.categories.index(category)
        if index >= len(self.categories):
            index = -1

        return index
