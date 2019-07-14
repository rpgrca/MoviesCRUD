"""TkinterEditor.py"""

from tkinter import *
from tkinter import ttk, messagebox
from Manager.Movies.MoviesManager import MoviesManager
from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.GeneralManager import GeneralManager
from Movie.Movie import Movie

class TkinterEditor(object):
    def set_general_manager(self, general_manager: GeneralManager):
        """Recibe el Manager general a usar"""
        self.__general_manager = general_manager
        self.clear_editor()
        self.__reload_movies()
        self.__load_categories()

#    def set_movies_manager(self, movies_manager: MoviesManager):
#        """Recibe el Manager de peliculas a usar"""
#        self.__general_manager.movies_manager = movies_manager
#        self.clear_editor()
#        self.__reload_movies()
#
#    def set_categories_manager(self, categories_manager: CategoriesManager):
#        """Recibe el Manager de categorias a usar"""
#        self.__general_manager.categories_manager = categories_manager
#        self.__load_categories()

#    def set_content_providers_manager(self, content_providers_manager: ContentProvidersManager):
#        """Recibe el Manager de content providers a usar"""
#        self.__content_providers_manager = content_providers_manager
#        self.__load_providers()

    def __get_selected_movie(self) -> Movie:
        """Retorna la pelicula actualmente seleccionada de la lista del editor"""
        if self.__movies_listbox.curselection():
            index = int(self.__movies_listbox.curselection()[0])
            value = self.__movies_listbox.get(index)
            identifier = int(value[:5])
            return self.__general_manager.movies_manager.get_movie(identifier)

    def __on_movies_listbox_selected(self, event):
        if self.__general_manager.movies_manager:
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
            self.parent_window.destroy()

    def __on_new_button_pressed(self):
        if self.__general_manager.movies_manager:
            self.clear_editor()
            self.enable_editor()
            self.__identifier.set(self.__general_manager.movies_manager.get_next_identifier())
            self.__enable_save_button()
            self.__disable_delete_button()

    def __verify_text(self, label: Label, textbox: Entry):
        can_save = False

        if textbox.get():
            label["fg"] = "black"
            can_save = True
        else:
            label["fg"] = "red"

        return can_save

    def __on_save_button_pressed(self):
        if self.__general_manager.movies_manager and self.__general_manager.categories_manager:
            can_save = True
            can_save = self.__verify_text(self.__title_label, self.__title) and can_save
            can_save = self.__verify_text(self.__description_label, self.__description) and can_save
            can_save = self.__verify_text(self.__releasedate_label, self.__releasedate) and can_save
            can_save = self.__verify_text(self.__director_label, self.__director) and can_save
            can_save = self.__verify_text(self.__category_label, self.__category) and can_save

            if can_save:
                category = self.__general_manager.categories_manager.create(self.__category.get())
                self.__reload_categories()
                movie = self.__general_manager.movies_manager.create(self.__title.get(), self.__description.get(), self.__releasedate.get(), self.__director.get(), category)
                self.__general_manager.movies_manager.get_movies().append(movie)
                self.clear_editor()
                self.__disable_save_button()
                self.disable_editor()
                self.__reload_movies()

    def __on_remove_button_pressed(self):
        if self.__general_manager.movies_manager and self.__movies_listbox.curselection():
            movie = self.__get_selected_movie()

            if movie:
                self.__general_manager.movies_manager.remove(movie.identifier)
                self.__reload_movies()
                self.clear_editor()
                self.disable_editor()
                self.__disable_delete_button()
                self.__disable_save_button()

    def __enable_delete_button(self):
        self.__remove_button["state"] = "normal"

    def __disable_delete_button(self):
        self.__remove_button["state"] = "disabled"

    def __enable_save_button(self):
        self.__save_button["state"] = "normal"

    def __disable_save_button(self):
        self.__save_button["state"] = "disabled"

    def __set_labels_color(self, color: str):
        controls = [self.__title_label, self.__description_label, self.__releasedate_label, self.__director_label, self.__category_label]
        for control in controls:
            control["fg"] = color

    def __set_textbox_state(self, state: str):
        controls = [self.__title_text, self.__description_text, self.__releasedate_text, self.__director_text]
        for control in controls:
            control["state"] = state

    def clear_editor(self):
        self.__identifier.set("")
        self.__title.set("")
        self.__description.set("")
        self.__releasedate.set("")
        self.__director.set("")
        self.__category.set("")

    def enable_editor(self):
        self.__set_textbox_state("normal")
        self.__categories_combo["state"] = "normal"
        self.__set_labels_color("black")

    def disable_editor(self):
        self.__set_textbox_state("readonly")
        self.__categories_combo["state"] = "disabled"
        self.__set_labels_color("black")

    def edit_movie(self, movie: Movie):
        self.__identifier.set(movie.identifier)
        self.__title.set(movie.title)
        self.__description.set(movie.description)
        self.__releasedate.set(movie.releasedate)
        self.__director.set(movie.director)
        self.__category.set(movie.category)

    def __reload_categories(self):
        if self.__general_manager.categories_manager:
            self.__categories_combo["values"] = self.__general_manager.categories_manager.get_categories()

    def __reload_movies(self):
        self.__movies_listbox.delete(0, END)

        if self.__general_manager.movies_manager:
            movies = self.__general_manager.movies_manager.get_movies()
            row_format = "{:<5}  {:>}"

            for movie in movies:
                self.__movies_listbox.insert(END, row_format.format(movie.identifier, movie.title, sp=" "*2))

    def __load_categories(self):
        if self.__general_manager.categories_manager:
            categories = self.__general_manager.categories_manager.get_categories()

            self.__categories_combo['values'] = categories

    def __load_content_providers(self):
        if self.__content_providers_manager:
            providers = self.__content_providers_manager.get_providers()

            for provider in providers:
                content_provider_menu = Menu(self.__menu)
                content_provider_menu.add_radiobutton(label=provider)

            self.__menu_frame

    def __init__(self, parent: Tk = None, **configs):
        self.parent_window = parent
        self.parent_window.wm_title("ABMC Peliculas")
        self.parent_window.protocol("WM_DELETE_WINDOW", self.__on_exit_button_pressed)
        self.parent_window.geometry("{}x{}".format(550, 350))

        # __main_window es la ventana principal
        self.__main_window = Frame(self.parent_window)
        self.__main_window.pack(expand=YES, fill=BOTH)

        self.__menu = Menu(self.parent_window)
        self.__settings_menu = Menu(self.__menu, tearoff=0)
        #self.__settings_menu.add_command(label="Ajustes", command=self.__on_settings_option_pressed)
        #self.__settings_menu.add_separator()
        self.__settings_menu.add_command(label="Salir", command=self.__on_exit_button_pressed) #self.parent_window.quit)

        self.__menu.add_cascade(label="Sistema", menu=self.__settings_menu)
        self.__menu.add_cascade(label="Ajustes")
        self.parent_window.config(menu=self.__menu)

        # __list_frame contiene a la lista de peliculas
        self.__list_frame = Frame(self.__main_window, height=300, width=250, borderwidth=7)
        self.__list_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        self.__scrollbar = Scrollbar(self.__list_frame, orient=VERTICAL)
        self.__movies_listbox = Listbox(self.__list_frame, yscrollcommand=self.__scrollbar.set)
        self.__scrollbar.config(command=self.__movies_listbox.yview)
        self.__scrollbar.pack(side=RIGHT, fill=Y)
        self.__movies_listbox.bind('<<ListboxSelect>>', self.__on_movies_listbox_selected)
        self.__movies_listbox.pack(side=LEFT, fill=BOTH, expand=YES)

        # __editor_frame contiene el editor de peliculas
        self.__editor_frame = Frame(self.__main_window, height=300, borderwidth=7)
        self.__editor_frame.pack(side=TOP, expand=NO, fill=X)

        self.__main_title_label = Label(self.__editor_frame, text="Datos de la pelicula", bg="green", borderwidth=7)
        self.__main_title_label.pack(side=TOP, expand=NO, fill=X)

        self.__identifier_container = Frame(self.__main_window, borderwidth=7)
        self.__identifier_container.pack(side=TOP, expand=NO, fill=X)
        self.__identifier_label = Label(self.__identifier_container, text="Identificador", borderwidth=7, width=15, anchor=W)
        self.__identifier_label.pack(side=LEFT, expand=NO)
        self.__identifier = StringVar()
        self.__identifier_text = Entry(self.__identifier_container, textvariable=self.__identifier, state="readonly")
        self.__identifier_text.pack(side=LEFT, expand=NO, fill=X)

        self.__title_container = Frame(self.__main_window, borderwidth=7)
        self.__title_container.pack(side=TOP, expand=NO, fill=X)
        self.__title_label = Label(self.__title_container, text="Nombre", borderwidth=7, width=15, anchor=W)
        self.__title_label.pack(side=LEFT, expand=NO)
        self.__title = StringVar()
        self.__title_text = Entry(self.__title_container, textvariable=self.__title, state="readonly")
        self.__title_text.pack(side=LEFT, expand=NO, fill=X)

        self.__description_container = Frame(self.__main_window, borderwidth=7)
        self.__description_container.pack(side=TOP, expand=NO, fill=X)
        self.__description_label = Label(self.__description_container, text="Descripcion", borderwidth=7, width=15, anchor=W)
        self.__description_label.pack(side=LEFT, expand=NO)
        self.__description = StringVar()
        self.__description_text = Entry(self.__description_container, textvariable=self.__description, state="readonly")
        self.__description_text.pack(side=LEFT, expand=NO, fill=X)

        self.__releasedate_container = Frame(self.__main_window, borderwidth=7)
        self.__releasedate_container.pack(side=TOP, expand=NO, fill=X)
        self.__releasedate_label = Label(self.__releasedate_container, text="Fecha de estreno", borderwidth=7, width=15, anchor=W)
        self.__releasedate_label.pack(side=LEFT, expand=NO)
        self.__releasedate = StringVar()
        self.__releasedate_text = Entry(self.__releasedate_container, textvariable=self.__releasedate, state="readonly")
        self.__releasedate_text.pack(side=LEFT, expand=NO, fill=X)

        self.__director_container = Frame(self.__main_window, borderwidth=7)
        self.__director_container.pack(side=TOP, expand=NO, fill=X)
        self.__director_label = Label(self.__director_container, text="Director", borderwidth=7, width=15, anchor=W)
        self.__director_label.pack(side=LEFT, expand=NO)
        self.__director = StringVar()
        self.__director_text = Entry(self.__director_container, textvariable=self.__director, state="readonly")
        self.__director_text.pack(side=LEFT, expand=NO, fill=X)

        self.__category_container = Frame(self.__main_window, borderwidth=7)
        self.__category_container.pack(side=TOP, expand=NO, fill=X)
        self.__category_label = Label(self.__category_container, text="Categoria", borderwidth=7, width=15, anchor=W)
        self.__category_label.pack(side=LEFT, expand=NO)
        self.__category = StringVar()
        self.__categories_combo = ttk.Combobox(self.__category_container, textvariable=self.__category, values=[], state="disabled")
        self.__categories_combo.bind('<<ComboboxSelected>>', self.__on_categories_combobox_selected)
        self.__categories_combo.pack(side=LEFT, expand=NO, fill=X)

        # __menu_frame contiene a los botones del menu
        self.__menu_frame = Frame(self.__main_window, height=50, borderwidth=7)
        self.__menu_frame.pack(side=TOP, expand=NO, fill=X)

        self.__new_button = Button(self.__menu_frame, text="Agregar", command=self.__on_new_button_pressed)
        self.__new_button.pack(side=LEFT)

        self.__save_button = Button(self.__menu_frame, text="Grabar", state=DISABLED, command=self.__on_save_button_pressed)
        self.__save_button.pack(side=LEFT)

        self.__remove_button = Button(self.__menu_frame, text="Borrar", state=DISABLED, command=self.__on_remove_button_pressed)
        self.__remove_button.pack(side=LEFT)

        self.__exit_button = Button(self.__menu_frame, text="Salir", command=self.__on_exit_button_pressed)
        self.__exit_button.pack(side=RIGHT)
