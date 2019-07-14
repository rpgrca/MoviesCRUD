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
    #manager.select_content_provider("json", "movies.json")
    manager.select_content_provider("memory")
    manager.load()

    editor.set_general_manager(manager)
    root.mainloop()

    manager.dump()
    manager.save()
