from typing import Any, List
from Manager.ContentProvider.ContentProvider import ContentProvider
from Manager.ContentProvider.FileContentProvider import FileContentProvider
from Manager.ContentProvider.ShelveContentProvider import ShelveContentProvider
from Manager.ContentProvider.EmptyContentProvider import EmptyContentProvider

class ContentProviderFactory:
    def create(self, content_provider_type: str, extra_data: List[Any]) -> ContentProvider:
        if content_provider_type == "memory":
            content_provider = ContentProvider()
            content_provider.set_items(extra_data)

        elif content_provider_type == "file":
            return FileContentProvider(extra_data[0])

        elif content_provider_type == "shelve":
            return ShelveContentProvider(extra_data[0])

        else:
            return EmptyContentProvider()
