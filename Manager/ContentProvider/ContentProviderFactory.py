from typing import Any
from Manager.ContentProvider.ContentProvider import ContentProvider
from Manager.ContentProvider.FileContentProvider import FileContentProvider
from Manager.ContentProvider.ShelveContentProvider import ShelveContentProvider
from Manager.ContentProvider.EmptyContentProvider import EmptyContentProvider

class ContentProviderFactory:
    def create(self, content_provider_type: str, *args: Any, **kw: Any) -> ContentProvider:
        if content_provider_type == "memory":
            return ContentProvider()

        elif content_provider_type == "file":
            return FileContentProvider(args)

        elif content_provider_type == "shelve":
            return ShelveContentProvider(args)

        else:
            return EmptyContentProvider()
