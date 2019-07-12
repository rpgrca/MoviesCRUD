from Manager.ContentProvider.ContentProvider import ContentProvider
from Manager.ContentProvider.FileContentProvider import FileContentProvider
from Manager.ContentProvider.ShelveContentProvider import ShelveContentProvider
from Manager.ContentProvider.EmptyContentProvider import EmptyContentProvider

class ContentProviderFactory:
    def create(self, content_provider_type: str) -> ContentProvider:
        if content_provider_type == "memory":
            return ContentProvider()

        elif content_provider_type == "file":
            return FileContentProvider("movies.txt")

        elif content_provider_type == "shelve":
            return ShelveContentProvider("movies.db")

        else:
            return EmptyContentProvider()
