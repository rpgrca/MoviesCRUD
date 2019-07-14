from tkinter import Tk
from Editor.TkinterEditor import TkinterEditor
from Manager.Movies.MoviesManager import MoviesManager
from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.ContentProvider.ContentProviderFactory import ContentProviderFactory
from Manager.ContentProvider.ContentProvidersManager import ContentProvidersManager
from Manager.GeneralManager import GeneralManager

if __name__ == '__main__':
    root = Tk()
    editor = TkinterEditor(root)

    manager = GeneralManager()
    manager.select_content_provider("json", "movies.json")
    manager.load()

    editor.set_general_manager(manager)
    root.mainloop()

    manager.dump()
    manager.save()


#if __name__ == '__main__':
#    root = Tk()
#    editor = TkinterEditor(root)
#
#    #content_provider = ContentProviderFactory.create("json", "movies.json")
#    #content_provider = ContentProviderFactory.create("shelve", "movies.db")
#    #content_provider = ContentProviderFactory.create("empty")
#    content_provider = ContentProviderFactory.create("memory")
#    #content_provider = ContentProviderFactory.create("csv", "movies.csv")
#
#    content_providers_manager = ContentProvidersManager()
#    categories_manager = CategoriesManager(content_provider)
#    movies_manager = MoviesManager(content_provider)
#
#    content_providers_manager.load()
#    categories_manager.load()
#    movies_manager.load()
#
#    editor.set_movies_manager(movies_manager)
#    editor.set_categories_manager(categories_manager)
#
#    root.mainloop()
#
#    categories_manager.dump()
#    movies_manager.dump()
#
#    content_provider.save()
