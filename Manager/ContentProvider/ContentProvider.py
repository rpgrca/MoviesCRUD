
class ContentProvider(object):
    def __init__(self):
        self.__items = []

    def load(self):
        self.__items = []

    def get_items(self):
        return self.__items

    def set_items(self, items):
        self.__items = items

    def save(self, items):
        self.__items = items

