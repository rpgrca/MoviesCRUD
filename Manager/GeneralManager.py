"""GeneralManager.py"""

from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.Movies.MoviesManager import MoviesManager
from Manager.ContentProvider.ContentProvidersManager import ContentProvidersManager
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider

class GeneralManager(ItemsManager):
    """Este manejador contiene al resto de los manejadores, ademas de una referencia al content provider activo"""
    def __init__(self):
        """Constructor"""
        self.__content_providers_manager = ContentProvidersManager()
        self.__content_providers_manager.load()
        self.__current_content_provider = None
        self.__categories_manager = None
        self.__movies_manager = None

    @property
    def movies_manager(self) -> MoviesManager:
        return self.__movies_manager

    @property
    def categories_manager(self) -> CategoriesManager:
        return self.__categories_manager

    @property
    def content_providers_manager(self) -> ContentProvidersManager:
        return self.__content_providers_manager

    @property
    def content_provider(self) -> ContentProvider:
        return self.__current_content_provider

    def select_content_provider(self, content_provider: str, extra_data: str = None):
        """Selecciona un nuevo Content Provider, inicializandolo con los datos indicados"""
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
