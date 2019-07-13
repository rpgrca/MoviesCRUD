"""EmptyContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class EmptyContentProvider(ContentProvider):
    def __init__(self):
        super(EmptyContentProvider, self).__init__()

    def get_name(self) -> str:
        return "Vacio (sin valores)"
