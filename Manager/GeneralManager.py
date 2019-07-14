"""GeneralManager.py"""

from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.Movies.MoviesManager import MoviesManager
from Manager.ContentProvider.ContentProvidersManager import ContentProvidersManager
from Manager.ItemsManager import ItemsManager

class GeneralManager(ItemsManager):
    def __init__(self):
        """Constructor"""
        self.__content_providers_manager = ContentProvidersManager()
        self.__current_content_provider = None
        self.__categories_manager = None
        self.__movies_manager = None

    @property
    def movies_manager(self):
        return self.__movies_manager

    @property
    def categories_manager(self):
        return self.__categories_manager

    @property
    def content_providers_manager(self):
        return self.__content_providers_manager

    def select_content_provider(self, content_provider: str, extra_data: str = None):
        self.__current_content_provider = self.__content_providers_manager.create(content_provider, extra_data)

    def load(self):
        """Inicializa todos los managers"""
        if self.__current_content_provider is None:
            self.select_content_provider("empty")

        self.__categories_manager = CategoriesManager(self.__current_content_provider)
        self.__categories_manager.load()
        self.__movies_manager = MoviesManager(self.__current_content_provider)
        self.__movies_manager.load()

    def dump(self):
        """Copia los elementos de los managers en el ContentProvider"""
        if self.__current_content_provider is not None:
            self.__categories_manager.dump()
            self.__movies_manager.dump()

    def save(self):
        """Graba los elementos del Content Provider"""
        if self.__current_content_provider is not None:
            self.__current_content_provider.save()
