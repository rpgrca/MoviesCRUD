"""ContentProvidersManager.py"""

from typing import List, Any
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider
from Manager.ContentProvider.ContentProviderFactory import ContentProviderFactory

class ContentProvidersManager(ItemsManager):
    """Manejador de Content Providers, posee una instancia de cada uno en memoria"""

    def __init__(self):
        """Constructor"""
        super(ContentProvidersManager, self).__init__(None)

    def create(self, content_provider: str, extra_data: str) -> ContentProvider:
        """Retorna el content provider indicado, creandolo en caso de no existir"""
        result = [x for x in self.items if x.key == content_provider]
        if result:
            return result[0]
        else:
            result = ContentProviderFactory.create(content_provider, extra_data)
            self.items.append(result)
            return result

    def load(self):
        # TODO: Podria ser a pedido para optimizar la creacion
        """Carga cada uno de los content providers disponibles"""
        content_providers = []
        for provider in ContentProviderFactory.get_providers():
            content_providers.append(ContentProviderFactory.create(provider))

        self.items = content_providers

    def get_providers(self) -> List[ContentProvider]:
        """Retorna la lista actual de content providers del Manager"""
        return super(ContentProvidersManager, self).items
