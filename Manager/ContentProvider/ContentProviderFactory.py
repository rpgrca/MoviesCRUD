from typing import Any, List
from Manager.ContentProvider.ContentProvider import ContentProvider
from Manager.ContentProvider.MemoryContentProvider import MemoryContentProvider
from Manager.ContentProvider.FileContentProvider import FileContentProvider
from Manager.ContentProvider.ShelveContentProvider import ShelveContentProvider
from Manager.ContentProvider.EmptyContentProvider import EmptyContentProvider
from Manager.ContentProvider.JSONContentProvider import JSONContentProvider
from Manager.ContentProvider.MySQLContentProvider import MySQLContentProvider
from Manager.ContentProvider.ZODBContentProvider import ZODBContentProvider
from Manager.ContentProvider.MongoDBContentProvider import MongoDBContentProvider

class ContentProviderFactory:
    @staticmethod
    def get_providers() -> List[str]:
        return [ "memory", "file", "json", "csv", "empty", "shelve", "mysql", "zodb", "mongodb" ]

    @staticmethod
    def create(content_provider_type: str, extra_data: Any = None) -> ContentProvider:
        content_provider_type = content_provider_type.lower()
        if content_provider_type == "memory":
            return MemoryContentProvider()

        elif content_provider_type == "file":
            return FileContentProvider(extra_data)

        elif content_provider_type == "json":
            return JSONContentProvider(extra_data)

        elif content_provider_type == "csv":
            return CSVContentProvider(extra_data)

        elif content_provider_type == "shelve":
            return ShelveContentProvider(extra_data)

        elif content_provider_type == "mysql":
            return MySQLContentProvider(extra_data)

        elif content_provider_type == "zodb":
            return ZODBContentProvider(extra_data)

        elif content_provider_type == "mongodb":
            return MongoDBContentProvider(extra_data)

        else:
            return EmptyContentProvider()
