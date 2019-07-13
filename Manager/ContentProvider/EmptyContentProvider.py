from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class EmptyContentProvider(ContentProvider):
    def __init__(self):
        super(EmptyContentProvider, self).__init__()

    def load(self):
        pass

    def save(self):
        pass
