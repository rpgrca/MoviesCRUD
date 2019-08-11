"""ContentProviderFactory.py"""

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
from Manager.ContentProvider.CSVContentProvider import CSVContentProvider
from Manager.ContentProvider.SQLiteContentProvider import SQLiteContentProvider

class ContentProviderFactory:
    """Fabrica para crear los Content Providers"""

    @staticmethod
    def get_providers() -> List[str]:
        """Retorna las llaves de todos los Content Providers disponibles"""
        return [MemoryContentProvider.KEY(),
                #FileContentProvider.KEY(),
                JSONContentProvider.KEY(),
                CSVContentProvider.KEY(),
                EmptyContentProvider.KEY(),
                ShelveContentProvider.KEY(),
                MySQLContentProvider.KEY(),
                ZODBContentProvider.KEY(),
                MongoDBContentProvider.KEY(),
                SQLiteContentProvider.KEY()]

    @staticmethod
    def create(content_provider_type: str, extra_data: Any = None) -> ContentProvider:
        """Crea un content provider del tipo indicado pasandole la informacion extra indicada"""

        content_provider_type = content_provider_type.lower()
        if content_provider_type == MemoryContentProvider.KEY():
            return MemoryContentProvider()

        elif content_provider_type == FileContentProvider.KEY():
            return FileContentProvider(extra_data)

        elif content_provider_type == JSONContentProvider.KEY():
            return JSONContentProvider(extra_data)

        elif content_provider_type == CSVContentProvider.KEY():
            return CSVContentProvider(extra_data)

        elif content_provider_type == ShelveContentProvider.KEY():
            return ShelveContentProvider(extra_data)

        elif content_provider_type == MySQLContentProvider.KEY():
            return MySQLContentProvider(extra_data)

        elif content_provider_type == ZODBContentProvider.KEY():
            return ZODBContentProvider(extra_data)

        elif content_provider_type == MongoDBContentProvider.KEY():
            return MongoDBContentProvider(extra_data)

        elif content_provider_type == SQLiteContentProvider.KEY():
            return SQLiteContentProvider(extra_data)

        else:
            return EmptyContentProvider()
