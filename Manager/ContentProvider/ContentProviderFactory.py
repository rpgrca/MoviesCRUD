from typing import Any, List
from Manager.ContentProvider.ContentProvider import ContentProvider
from Manager.ContentProvider.FileContentProvider import FileContentProvider
from Manager.ContentProvider.ShelveContentProvider import ShelveContentProvider
from Manager.ContentProvider.EmptyContentProvider import EmptyContentProvider

class ContentProviderFactory:
    __instance = None
    
    @staticmethod
    def get_singleton():
        if ContentProviderFactory.__instance == None:
            ContentProviderFactory()

        return ContentProviderFactory.__instance

    def __init__(self):
        if ContentProviderFactory.__instance == None:
        #    raise Exception("Singletons no pueden crearse")
        #else:
            ContentProviderFactory.__instance = self

    def create(self, content_provider_type: str, extra_data: Any) -> ContentProvider:
        if content_provider_type == "memory":
            content_provider = ContentProvider()
            content_provider.set_items(extra_data)
            return content_provider

        elif content_provider_type == "file":
            return FileContentProvider(extra_data)

        elif content_provider_type == "shelve":
            return ShelveContentProvider(extra_data)

        else:
            return EmptyContentProvider()
