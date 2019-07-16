"""ContentProvidersManager.py"""

from typing import List, Any
from Manager.ItemsManager import ItemsManager
from Manager.ContentProvider.ContentProvider import ContentProvider
from Manager.ContentProvider.ContentProviderFactory import ContentProviderFactory

class ContentProvidersManager(ItemsManager):
    def __init__(self):
        """Constructor"""
        super(ContentProvidersManager, self).__init__(None)

    def create(self, content_provider: str, extra_data: str) -> ContentProvider:
        result = [x for x in self.items if x.key == content_provider]
        if result:
            return result[0]
        else:
            return ContentProviderFactory.create(content_provider, extra_data)

    def load(self):
        """Carga cada uno de los content providers disponibles"""
        content_providers = []
        for provider in ContentProviderFactory.get_providers():
            content_providers.append(ContentProviderFactory.create(provider))

        self.items = content_providers

    def get_providers(self) -> List[ContentProvider]:
        """Retorna la lista actual de content providers del Manager"""
        return super(ContentProvidersManager, self).items
