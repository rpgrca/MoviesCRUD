from tkinter import Tk
from Editor.TkinterEditor import Editor
from Manager.Movies.MoviesManager import MoviesManager
from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.Categories.CategoriesMemoryContentProvider import CategoriesContentProvider
from Manager.Movies.MoviesMemoryContentProvider import MoviesContentProvider
from Manager.ContentProvider.ContentProviderFactory import ContentProviderFactory

if __name__ == '__main__':
    root = Tk()
    editor = Editor(root)

    content_provider = ContentProviderFactory.create("memory")
    categories_manager = CategoriesManager(content_provider)
    movies_manager = MoviesManager(content_provider)

    categories_manager.load()
    movies_manager.load()

    editor.set_movies_manager(movies_manager)
    editor.set_categories_manager(categories_manager)

    root.mainloop()

    categories_manager.save()
    movies_manager.save()
