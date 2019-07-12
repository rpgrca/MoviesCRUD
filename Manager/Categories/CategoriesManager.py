from typing import List, Any
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider

### tpd
class CategoriesManager(ItemsManager):
    def __init__(self, content_provider: ContentProvider):
        super(CategoriesManager, self).__init__(content_provider)

    def get_categories(self) -> List[Any]:
        return super(CategoriesManager, self).get_items()

    def create(self, category: str) -> str:
        if category not in self.get_items():
            self.get_items().append(category)

        return category

    def get_category_index(self, category: str) -> int:
        index = self.get_items().index(category)
        if index >= len(self.get_items()):
            index = -1

        return index
