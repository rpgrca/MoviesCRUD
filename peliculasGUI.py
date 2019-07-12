from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

class Movie(object):
    def __init__(self, identifier, title, description, releasedate, director, category):
        self.identifier = identifier
        self.title = title
        self.description = description
        self.releasedate = releasedate
        self.director = director
        self.category = category

    def __str__(self):
        return 'Id: {0}, Titulo: {1}, Desc: {2}, Fecha: {3}, Autor: {4}'.format(self.identifier, self.title, self.description, self.releasedate, self.director)

class ContentProvider(object):
    def load(self):
        pass

    def get_items(self):
        pass

    def save(self, items):
        pass

class MemoryContentProvider(ContentProvider):
    def __init__(self):
        super(MemoryContentProvider, self).__init__()
        self.__items = []

    def get_items(self):
        return self.__items

    def save(self, items):
        self.__items = items

class FileContentProvider(ContentProvider):
    def __init__(self, filename):
        super(FileContentProvider, self).__init__()
        self.__filename = filename

    def load(self):
        # TODO: Cargar items del archivo
        pass

    def get_items(self):
        return self.__items

    def save(self, items):
        # TODO: Grabar items del archivo
        pass

class ShelveContentProvider(ContentProvider):
    def __init__(self, database):
        super(ShelveContentProvider, self).__init__()
        self.__database = database

    def load(self):
        # TODO: Cargar items de la base
        pass

    def get_items(self):
        return self.__items

    def save(self, items):
        # TODO: Cargar items de la base
        pass

class EmptyContentProvider(ContentProvider):
    def __init__(self):
        super(EmptyContentProvider, self).__init__()

    def load(self):
        pass

    def get_items(self):
        return self.__items

    def save(self, items):
        pass

class ContentProviderFactory:
    def create(self, content_provider_type):
        if content_provider_type == "memory":
            return MemoryContentProvider()

        elif content_provider_type == "file":
            return FileContentProvider()

        elif content_provider_type == "shelve":
            return ShelveContentProvider()

        else:
            return EmptyContentProvider()

class CategoriesMemoryContentProvider(MemoryContentProvider):
    def __init__(self):
        super(CategoriesMemoryContentProvider, self).__init__()

    def load(self):
        self.__items = ["Accion", "Comedia", "Suspenso", "Terror"]


class MoviesMemoryContentProvider(MemoryContentProvider):
    def __init__(self):
        super(MoviesMemoryContentProvider, self).__init__()

    def load(self):
        self.__items = [ Movie(1, "The Terminator", "American science fiction film", '1984-10-26', "James Cameron", "Accion"),
                         Movie(2, "RoboCop", "Crime/Sci-fi", '1987-09-17', "Paul Verhoeven", "Accion"),
                         Movie(3, "A Nightmare on Elm Street", "Mystery/Slasher", '1984-11-09', "Wes Craven", "Suspenso"),
                         Movie(4, "Friday the 13th", "Slasher film", '1980-05-09', "Sean S. Cunningham", "Terror"),
                         Movie(5, "Back to the Future", "Fantasy/Sci-fi", '1985-12-26', "Robert Zemeckis", "Comedia") ]



class ItemsManager(object):
    def __init__(self, content_provider):
        self.content_provider = content_provider
        self.items = []
        self.__initialized = False

    def load(self):
        if not self.__initialized and self.content_provider:
            self.content_provider.load()
            self.items = self.content_provider.get_items()
            self.__initialized = True

    def get_items(self):
        return self.items

    def save(self):
        if self.content_provider:
            self.content_provider.save(self.items)

class CategoriesManager(ItemsManager):
    def __init__(self, content_provider):
        super(CategoriesManager, self).__init__(content_provider)

    def get_categories(self):
        return super(CategoriesManager, self).load()

    def create(self, category):
        if category not in self.__categories:
            self.__categories.append(category)

        return category

    def get_category_index(self, category):
        index = self.__categories.index(category)
        if index >= len(self.__categories):
            index = -1

        return index


class MemoryCategoriesManager(CategoriesManager):
    def __init__(self):
        super(MemoryCategoriesManager, self).__init__(CategoriesMemoryContentProvider())


class MoviesManager(ItemsManager):
    def __init__(self, content_provider):
        super(MoviesManager, self).__init__(content_provider)

    def create(self, title, description, releasedate, director, category):
        return Movie(self.get_next_identifier(), title, description, releasedate, director, category)

    def remove(self, identifier):
        self.__items = list(filter(lambda x : x.identifier != identifier, self.__items))

    def get_movies(self):
        return super(MoviesManager, self).get_items()

    def get_movie(self, identifier):
        result = list(filter(lambda x : x.identifier == identifier, self.__items))
        if result and len(result) > 0:
            return result[0]
 
        return None

    def get_next_identifier(self):
        if self.__items:
            return self.__items[-1].identifier + 1
        else:
            return 1

class MemoryMoviesManager(MoviesManager):
    def __init__(self):
        super(MemoryMoviesManager, self).__init__(MoviesMemoryContentProvider())


class Editor(object):
    def set_movies_manager(self, movies_manager):
        self.__movies_manager = movies_manager
        self.clear_editor()
        self.__reload_movies()

    def set_categories_manager(self, categories_manager):
        self.__categories_manager = categories_manager
        self.__load_categories()

    def __get_selected_movie(self):
        if self.movies_listbox.curselection():
            index = int(self.movies_listbox.curselection()[0])
            value = self.movies_listbox.get(index)
            identifier = int(value[:5])
            return self.__movies_manager.get_movie(identifier)

    def __on_movies_listbox_selected(self, event):
        if self.__movies_manager:
            w = event.widget
            if w.curselection():
                self.__enable_delete_button()
                movie = self.__get_selected_movie()
                if movie:
                    self.__disable_save_button()
                    self.disable_editor()
                    self.edit_movie(movie)

    def __on_categories_combobox_selected(self, event):
        pass

    def __on_exit_button_pressed(self):
        if messagebox.askokcancel("Salir", "Esta seguro que desea terminar la aplicacion?"):
            pass

    def __on_new_button_pressed(self):
        if self.__movies_manager:
            self.clear_editor()
            self.enable_editor()
            self.__identifier.set(self.__movies_manager.get_next_identifier())
            self.__enable_save_button()

    def __verify_text(self, label, textbox):
        can_save = False

        if textbox.get():
            label["fg"] = "black"
            can_save = True
        else:
            label["fg"] = "red"

        return can_save

    def __on_save_button_pressed(self):
        if self.__movies_manager and self.__categories_manager:
            can_save = True
            can_save = self.__verify_text(self.title_label, self.__title) and can_save
            can_save = self.__verify_text(self.description_label, self.__description) and can_save
            can_save = self.__verify_text(self.releasedate_label, self.__releasedate) and can_save
            can_save = self.__verify_text(self.director_label, self.__director) and can_save
            can_save = self.__verify_text(self.category_label, self.__category) and can_save

            if can_save:
                category = self.__categories_manager.create(self.__category.get())
                self.__reload_categories()
                movie = self.__movies_manager.create(self.__title.get(), self.__description.get(), self.__releasedate.get(), self.__director.get(), category)
                self.__movies_manager.get_movies().append(movie)
                self.clear_editor()
                self.__disable_save_button()
                self.disable_editor()
                self.__reload_movies()

    def __on_remove_button_pressed(self):
        if self.__movies_manager and self.movies_listbox.curselection():
            movie = self.__get_selected_movie()

            if movie:
                self.__movies_manager.remove(movie.identifier)
                self.__reload_movies()
                self.clear_editor()
                self.disable_editor()
                self.__disable_delete_button()
                self.__disable_save_button()

    def __enable_delete_button(self):
        self.remove_button["state"] = "normal"

    def __disable_delete_button(self):
        self.remove_button["state"] = "disabled"

    def __enable_save_button(self):
        self.save_button["state"] = "normal"

    def __disable_save_button(self):
        self.save_button["state"] = "disabled"

    def clear_editor(self):
        self.__identifier.set("")
        self.__title.set("")
        self.__description.set("")
        self.__releasedate.set("")
        self.__director.set("")
        self.__category.set("")
        #self.categories_combo.set("")

    def __set_labels_color(self, color):
        controls = [self.title_label, self.description_label, self.releasedate_label, self.director_label, self.category_label]
        for control in controls:
            control["fg"] = color

    def __set_textbox_state(self, state):
        controls = [self.title_text, self.description_text, self.releasedate_text, self.director_text]
        for control in controls:
            control["state"] = state

    def enable_editor(self):
        self.__set_textbox_state("normal")
        self.categories_combo["state"] = "normal"
        self.__set_labels_color("black")

    def disable_editor(self):
        self.__set_textbox_state("readonly")
        self.categories_combo["state"] = "disabled"
        self.__set_labels_color("black")

    def edit_movie(self, movie):
        self.__identifier.set(movie.identifier)
        self.__title.set(movie.title)
        self.__description.set(movie.description)
        self.__releasedate.set(movie.releasedate)
        self.__director.set(movie.director)
        self.__category.set(movie.category)
        #index = self.__categories_manager.get_category_index(movie.category)
        #if index > 0:
        #    self.categories_combo.current(index)

    def __reload_categories(self):
        if self.__categories_manager:
            self.categories_combo["values"] = self.__categories_manager.get_categories()

    def __reload_movies(self):
        self.movies_listbox.delete(0, END)

        if self.__movies_manager:
            movies = self.__movies_manager.get_movies()
            row_format = "{:<5}  {:>}"

            for movie in movies:
                self.movies_listbox.insert(END, row_format.format(movie.identifier, movie.title, sp=" "*2))

    def __load_categories(self):
        if self.__categories_manager:
            categories = self.__categories_manager.get_categories()

            self.categories_combo['values'] = categories


    def __init__(self, parent=None, **configs):
        self.__movies_manager = None
        self.__categories_manager = None

        self.parent_window = parent
        self.parent_window.geometry("{}x{}".format(550, 350))

        # main_window es la ventana principal
        self.main_window = Frame(self.parent_window)
        self.main_window.pack(expand=YES, fill=BOTH)

        # list_frame contiene a la lista de peliculas
        self.list_frame = Frame(self.main_window, height=300, width=250, borderwidth=7)
        self.list_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        self.scrollbar = Scrollbar(self.list_frame, orient=VERTICAL)
        self.movies_listbox = Listbox(self.list_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.movies_listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.movies_listbox.bind('<<ListboxSelect>>', self.__on_movies_listbox_selected)
        self.movies_listbox.pack(side=LEFT, fill=BOTH, expand=YES)

        # editor_frame contiene el editor de peliculas
        self.editor_frame = Frame(self.main_window, height=300, borderwidth=7)
        self.editor_frame.pack(side=TOP, expand=NO, fill=X)

        self.main_title_label = Label(self.editor_frame, text="Datos de la pelicula", bg="green", borderwidth=7)
        self.main_title_label.pack(side=TOP, expand=NO, fill=X)

        self.identifier_container = Frame(self.main_window, borderwidth=7)
        self.identifier_container.pack(side=TOP, expand=NO, fill=X)
        self.identifier_label = Label(self.identifier_container, text="Identificador", borderwidth=7, width=15, anchor=W)
        self.identifier_label.pack(side=LEFT, expand=NO)
        self.__identifier = StringVar()
        self.identifier_text = Entry(self.identifier_container, textvariable=self.__identifier, state="readonly")
        self.identifier_text.pack(side=LEFT, expand=NO, fill=X)

        self.title_container = Frame(self.main_window, borderwidth=7)
        self.title_container.pack(side=TOP, expand=NO, fill=X)
        self.title_label = Label(self.title_container, text="Nombre", borderwidth=7, width=15, anchor=W)
        self.title_label.pack(side=LEFT, expand=NO)
        self.__title = StringVar()
        self.title_text = Entry(self.title_container, textvariable=self.__title, state="readonly")
        self.title_text.pack(side=LEFT, expand=NO, fill=X)

        self.description_container = Frame(self.main_window, borderwidth=7)
        self.description_container.pack(side=TOP, expand=NO, fill=X)
        self.description_label = Label(self.description_container, text="Descripcion", borderwidth=7, width=15, anchor=W)
        self.description_label.pack(side=LEFT, expand=NO)
        self.__description = StringVar()
        self.description_text = Entry(self.description_container, textvariable=self.__description, state="readonly")
        self.description_text.pack(side=LEFT, expand=NO, fill=X)

        self.releasedate_container = Frame(self.main_window, borderwidth=7)
        self.releasedate_container.pack(side=TOP, expand=NO, fill=X)
        self.releasedate_label = Label(self.releasedate_container, text="Fecha de estreno", borderwidth=7, width=15, anchor=W)
        self.releasedate_label.pack(side=LEFT, expand=NO)
        self.__releasedate = StringVar()
        self.releasedate_text = Entry(self.releasedate_container, textvariable=self.__releasedate, state="readonly")
        self.releasedate_text.pack(side=LEFT, expand=NO, fill=X)

        self.director_container = Frame(self.main_window, borderwidth=7)
        self.director_container.pack(side=TOP, expand=NO, fill=X)
        self.director_label = Label(self.director_container, text="Director", borderwidth=7, width=15, anchor=W)
        self.director_label.pack(side=LEFT, expand=NO)
        self.__director = StringVar()
        self.director_text = Entry(self.director_container, textvariable=self.__director, state="readonly")
        self.director_text.pack(side=LEFT, expand=NO, fill=X)

        self.category_container = Frame(self.main_window, borderwidth=7)
        self.category_container.pack(side=TOP, expand=NO, fill=X)
        self.category_label = Label(self.category_container, text="Categoria", borderwidth=7, width=15, anchor=W)
        self.category_label.pack(side=LEFT, expand=NO)
        self.__category = StringVar()
        self.categories_combo = ttk.Combobox(self.category_container, textvariable=self.__category, values=[], state="disabled")
        self.categories_combo.bind('<<ComboboxSelected>>', self.__on_categories_combobox_selected)
        self.categories_combo.pack(side=LEFT, expand=NO, fill=X)

        # menu_frame contiene a los botones del menu
        self.menu_frame = Frame(self.main_window, height=50, borderwidth=7)
        self.menu_frame.pack(side=TOP, expand=NO, fill=X)

        self.new_button = Button(self.menu_frame, text="Agregar", command=self.__on_new_button_pressed)
        self.new_button.pack(side=LEFT)

        self.save_button = Button(self.menu_frame, text="Grabar", state=DISABLED, command=self.__on_save_button_pressed)
        self.save_button.pack(side=LEFT)

        #self.remove_button = Button(self.menu_frame, text="Borrar", state=DISABLED, command=lambda lb=self.movies_listbox: lb.delete(ANCHOR))
        self.remove_button = Button(self.menu_frame, text="Borrar", state=DISABLED, command=self.__on_remove_button_pressed)
        self.remove_button.pack(side=LEFT)

        self.exit_button = Button(self.menu_frame, text="Salir", command=self.__on_exit_button_pressed)
        self.exit_button.pack(side=RIGHT)

if __name__ == '__main__':
    root = Tk()
    editor = Editor(root)

    categories_manager = MemoryCategoriesManager()
    movies_manager = MemoryMoviesManager()

    categories_manager.load()
    movies_manager.load()

    editor.set_movies_manager(movies_manager)
    editor.set_categories_manager(categories_manager)

    root.mainloop()

    categories_manager.save()
    movies_manager.save()
