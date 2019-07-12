from Manager.ItemsManager import ItemsManager

### tpd
class CategoriesManager(ItemsManager):
    def __init__(self, content_provider):
        super(CategoriesManager, self).__init__(content_provider)

    def get_categories(self):
        return super(CategoriesManager, self).get_items()

    def create(self, category):
        if category not in self.get_items():
            self.get_items().append(category)

        return category

    def get_category_index(self, category):
        index = self.get_items().index(category)
        if index >= len(self.get_items()):
            index = -1

        return index
