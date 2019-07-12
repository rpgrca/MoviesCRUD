from tkinter import Tk
from Editor.TkinterEditor import Editor
from Manager.Movies.MoviesManager import MoviesManager
from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.ContentProvider.ContentProviderFactory import ContentProviderFactory
from Movie.Movie import Movie

if __name__ == '__main__':
    root = Tk()
    editor = Editor(root)

    categories_manager = CategoriesManager(ContentProviderFactory.create("memory", [ "Accion", "Comedia", "Suspenso", "Terror" ]))
    movies_manager = MoviesManager(ContentProviderFactory.create("memory", [ Movie(1, "The Terminator", "American science fiction film", '1984-10-26', "James Cameron", "Accion"),
                         Movie(2, "RoboCop", "Crime/Sci-fi", '1987-09-17', "Paul Verhoeven", "Accion"),
                         Movie(3, "A Nightmare on Elm Street", "Mystery/Slasher", '1984-11-09', "Wes Craven", "Suspenso"),
                         Movie(4, "Friday the 13th", "Slasher film", '1980-05-09', "Sean S. Cunningham", "Terror"),
                         Movie(5, "Back to the Future", "Fantasy/Sci-fi", '1985-12-26', "Robert Zemeckis", "Comedia") ]))

    categories_manager.load()
    movies_manager.load()

    editor.set_movies_manager(movies_manager)
    editor.set_categories_manager(categories_manager)

    root.mainloop()

    categories_manager.save()
    movies_manager.save()
