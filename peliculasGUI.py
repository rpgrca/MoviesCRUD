from tkinter import Tk
from Editor.TkinterEditor import Editor
from Manager.Movies.MoviesManager import MoviesManager
from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.Categories.CategoriesMemoryContentProvider import CategoriesMemoryContentProvider
from Manager.Movies.MoviesMemoryContentProvider import MoviesMemoryContentProvider

if __name__ == '__main__':
    root = Tk()
    editor = Editor(root)

    categories_manager = CategoriesManager(CategoriesMemoryContentProvider())
    movies_manager = MoviesManager(MoviesMemoryContentProvider())

    categories_manager.load()
    movies_manager.load()

    editor.set_movies_manager(movies_manager)
    editor.set_categories_manager(categories_manager)

    root.mainloop()

    categories_manager.save()
    movies_manager.save()
