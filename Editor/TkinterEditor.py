"""TkinterEditor.py"""

import datetime
from tkinter import *
from tkinter import ttk, messagebox
from Editor.SettingsEditor import SettingsEditor
from Editor.WindowsUtilities import WindowsUtilities
from Manager.Movies.MoviesManager import MoviesManager
from Manager.Categories.CategoriesManager import CategoriesManager
from Manager.GeneralManager import GeneralManager
from Movie.Movie import Movie

class TkinterEditor(object):
    """Ventana principal de la aplicacion"""
    LABEL_OK_COLOR = "black"
    LABEL_ERROR_COLOR = "red"
    DATE_FORMAT = '%Y-%m-%d'
    IDENTIFIER_SIZE = 5 # Cantidad de espacios entre el id y el nombre de la pelicula
    LISTBOX_ITEM_FORMAT = "{:<" + str(IDENTIFIER_SIZE) + "}  {:>}" # Formato a usar para mostrar las peliculas
    APPLICATION_TITLE = "ABMC Peliculas"
    WINDOW_WIDTH = 550
    WINDOW_HEIGHT = 350
    EXIT_MENU = "Salir"
    SETTINGS_MENU = "Ajustes"
    SYSTEM_MENU = "Sistema"
    MAIN_TITLE = "Datos de la pelicula"
    IDENTIFIER_LABEL = "Identificador"
    TITLE_LABEL = "Titulo"
    DESCRIPTION_LABEL = "Description"
    RELEASE_DATE_LABEL = "Fecha de estreno"
    DIRECTOR_LABEL = "Director"
    CATEGORY_LABEL = "Categoria"
    ADD_BUTTON_CAPTION = "Agregar"
    CANCEL_BUTTON_CAPTION = "Cancelar"
    REMOVE_BUTTON_CAPTION = "Borrar"
    SAVE_BUTTON_CAPTION = "Grabar"
    EXIT_BUTTON_CAPTION = "Salir"
    CONFIRM_QUESTION = "Esta seguro que desea terminar la aplicacion?"
    QUESTION_NOT_IMPLEMENTED_TITLE = "Sin implementar"
    QUESTION_NOT_IMPLEMENTED_MESSAGE = "Esta funcionalidad no esta implementada aun"
    QUESTION_RELOAD_TITLE = "Recargar"
    QUESTION_RELOAD_MESSAGE = "Esta seguro que desea cambiar el proveedor?"
    CONFIGURATION_MENU = "Configuracion"
    EDIT_CONTEXT_MENU = "Editar"
    DELETE_CONTEXT_MENU = "Borrar"
    SELECT_ALL_CONTEXT_MENU = "Seleccionar todo"

    def set_general_manager(self, general_manager: GeneralManager):
        """Recibe el Manager general a usar"""
        self.__general_manager = general_manager
        self.__reload_movies()
        self.__reload_categories()
        self.__load_content_providers()
        self.clear_editor()

    def __switch_content_provider(self, content_provider: str, save: bool):
        """Cambia el content provider a otro"""
        # TODO: Si falla cambiar la conexion, al volver ya esta cerrada la vieja
        if save:
            self.__general_manager.dump()
            self.__general_manager.save()

        self.__general_manager.select_content_provider(content_provider)
        self.__general_manager.load()
        self.__reload_movies()
        self.__reload_categories()
        self.clear_editor()

    def __get_selected_movie(self) -> Movie:
        """Retorna la pelicula actualmente seleccionada de la lista del editor"""
        if self.__movies_listbox.curselection():
            index = int(self.__movies_listbox.curselection()[0])
            value = self.__movies_listbox.get(index)
            identifier = int(value[:TkinterEditor.IDENTIFIER_SIZE])
            return self.__general_manager.movies_manager.get_movie(identifier)

    def __on_not_implemented(self):
        """Callback para recordar que algo no esta implementado"""
        messagebox.showwarning(TkinterEditor.QUESTION_NOT_IMPLEMENTED_TITLE, TkinterEditor.QUESTION_NOT_IMPLEMENTED_MESSAGE)

    def __on_configuration_clicked(self):
        """Callback llamada al seleccionar la opcion Configuracion del menu"""
        popup = Toplevel()
        editor = SettingsEditor(popup)
        editor.configure(self.__general_manager.content_providers_manager, self.__general_manager.content_provider)

        popup.grab_set()
        popup.focus_set()
        popup.wait_window()

    def __on_movies_listbox_selected(self, event):
        """Callback llamada cuando se selecciona un elemento de la lista"""
        if self.__general_manager.movies_manager:
            w = event.widget
            if w.curselection():
                self.__enable_delete_button()
                movie = self.__get_selected_movie()
                if movie:
                    self.__on_cancel_button_pressed()
                    self.edit_movie(movie)
    
    def __on_movies_listbox_right_click(self, event):
        """Callback llamada cuando se hace click con el boton derecho sobre la lista"""
        try:
            self.__movies_listbox_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.__movies_listbox_menu.grab_release()

    def __on_cp_menu_item_selected(self):
        """Callback llamada al seleccionar un content provider"""
        if messagebox.askokcancel(TkinterEditor.QUESTION_RELOAD_TITLE, TkinterEditor.QUESTION_RELOAD_MESSAGE):
            new_connection = self.__selected_content_provider.get()
            old_connection = self.__previous_content_provider

            try:
                self.__switch_content_provider(new_connection, True)
                self.__previous_content_provider = new_connection
            except Exception as err:
                messagebox.showerror(title="Error", message=err)
                #self.__general_manager.select_content_provider(old_connection)
                self.__switch_content_provider(old_connection, False)
                self.__previous_content_provider = old_connection
                self.__selected_content_provider.set(self.__previous_content_provider)
        else:
            self.__selected_content_provider.set(self.__previous_content_provider)

    def __on_categories_combobox_selected(self, event):
        """Callback llamada al seleccionar un elemento del combo"""
        pass

    def __on_exit_button_pressed(self):
        """Callback llamada al querer salir, preguntando antes de hacerlo"""
        if messagebox.askokcancel(TkinterEditor.EXIT_MENU, TkinterEditor.CONFIRM_QUESTION):
            self.parent_window.destroy()

    def __on_new_button_pressed(self):
        # TODO: Deberia deshabilitarse cuando se presiona una vez? Si no preguntar antes de borrar el editor
        """Callback llamada al presionar el boton para crear una nueva pelicula"""
        if self.__general_manager.movies_manager:
            self.clear_editor()
            self.enable_editor()
            self.__identifier.set(self.__general_manager.movies_manager.get_next_identifier())
            self.__enable_save_button()
            self.__disable_delete_button()
            self.__new_button.configure(text=TkinterEditor.CANCEL_BUTTON_CAPTION, command=self.__on_cancel_button_pressed)

    def __on_cancel_button_pressed(self):
        """Callback llamada al presionar el boton para cancelar"""
        if self.__general_manager.movies_manager:
            self.clear_editor() # TODO: Tal vez deberia llamar a edit_movie
            self.disable_editor()
            self.__disable_save_button()
            self.__enable_delete_button()
            self.__new_button.configure(text=TkinterEditor.ADD_BUTTON_CAPTION, command=self.__on_new_button_pressed)

    def __on_save_button_pressed(self):
        """Callback llamada al presionar el boton de grabar"""
        if self.__general_manager.movies_manager and self.__general_manager.categories_manager:
            # Normalmente se utiliza al reves pero quiero que se ejecute la funcion sin importar
            # si ya fallo otro anteriormente para colorear todas las etiquetas 
            can_save = True
            can_save = self.__verify_text(self.__title_label, self.__title) and can_save
            can_save = self.__verify_text(self.__description_label, self.__description) and can_save
            can_save = self.__verify_date(self.__releasedate_label, self.__releasedate) and can_save
            can_save = self.__verify_text(self.__director_label, self.__director) and can_save
            can_save = self.__verify_text(self.__category_label, self.__category) and can_save

            if can_save:
                category = self.__general_manager.categories_manager.create(self.__category.get())
                self.__reload_categories()
                movie = self.__general_manager.movies_manager.get_movie(self.__identifier.get())
                if movie:
                    movie.title = self.__title.get()
                    movie.description = self.__description.get()
                    movie.releasedate = self.__releasedate.get()
                    movie.director = self.__director.get()
                    movie.category = category
                else:
                    movie = self.__general_manager.movies_manager.create(self.__title.get(), self.__description.get(), self.__releasedate.get(), self.__director.get(), category)
                    self.__general_manager.movies_manager.movies.append(movie)

                self.__on_cancel_button_pressed()
                self.__reload_movies()

    def __on_edit_movie(self):
        """Callback llamada al editar una pelicula desde el menu contextual"""
        movie = self.__get_selected_movie()
        if movie:
            self.clear_editor()
            self.enable_editor()
            self.edit_movie(movie)
            self.__enable_save_button()
            self.__disable_delete_button()
            self.__new_button.configure(text=TkinterEditor.CANCEL_BUTTON_CAPTION, command=self.__on_cancel_button_pressed)

    def __on_remove_movie(self):
        """Callback llamada cuando se presiona el boton de borrar una pelicula"""
        if self.__general_manager.movies_manager and self.__movies_listbox.curselection():
            movie = self.__get_selected_movie()

            if movie:
                self.__general_manager.movies_manager.remove(movie.identifier)
                self.__reload_movies()
                self.clear_editor()
                self.disable_editor()
                self.__disable_delete_button()
                self.__disable_save_button()

    def __verify_text(self, label: Label, textbox: Entry) -> bool:
        """Cambia el color del Label si el usuario no completo el textbox retornando False"""
        can_save = False

        if textbox.get():
            label['fg'] = TkinterEditor.LABEL_OK_COLOR
            can_save = True
        else:
            label['fg'] = TkinterEditor.LABEL_ERROR_COLOR

        return can_save

    def __verify_date(self, label: Label, textbox: Entry) -> bool:
        """Cambia el color del Label si la fecha de estreno es incorrecta retornando False"""
        can_save = False

        try:
            datetime.datetime.strptime(textbox.get(), TkinterEditor.DATE_FORMAT)
            label['fg'] = TkinterEditor.LABEL_OK_COLOR
            can_save = True
        except ValueError:
            label['fg'] = TkinterEditor.LABEL_ERROR_COLOR

        return can_save

    def __enable_delete_button(self):
        """Habilita el boton de borrado de peliculas"""
        self.__remove_button['state'] = 'normal'

    def __disable_delete_button(self):
        """Deshabilita el boton de borrado de peliculas"""
        self.__remove_button['state'] = 'disabled'

    def __enable_save_button(self):
        """Habilita el boton de grabado de peliculas"""
        self.__save_button['state'] = 'normal'

    def __disable_save_button(self):
        """Deshabilita el boton de grabado de peliculas"""
        self.__save_button['state'] = 'disabled'

    def __set_labels_color(self, color: str):
        """Cambia el color de las etiquetas de los campos de las peliculas al seleccionado"""
        controls = [self.__title_label, self.__description_label, self.__releasedate_label, self.__director_label, self.__category_label]
        for control in controls:
            control['fg'] = color

    def __set_textbox_state(self, state: str):
        """Cambia el estado de los editores de texto de peliculas al seleccionado"""
        controls = [self.__title_text, self.__description_text, self.__releasedate_text, self.__director_text]
        for control in controls:
            control['state'] = state

    def clear_editor(self):
        """Limpia todos los campos del editor de peliculas"""
        self.__identifier.set("")
        self.__title.set("")
        self.__description.set("")
        self.__releasedate.set("")
        self.__director.set("")
        self.__category.set("")

    def enable_editor(self):
        """Habilita el editor para poder modificar o crear una pelicula"""
        self.__set_textbox_state('normal')
        self.__categories_combo['state'] = 'normal'
        self.__set_labels_color('black')

    def disable_editor(self):
        """Deshabilita el editor de peliculas"""
        self.__set_textbox_state('readonly')
        self.__categories_combo['state'] = 'disabled'
        self.__set_labels_color('black')

    def edit_movie(self, movie: Movie):
        """Edita la pelicula dada, colocando los datos de los campos en los controles correspondientes"""
        self.__identifier.set(movie.identifier)
        self.__title.set(movie.title)
        self.__description.set(movie.description)
        self.__releasedate.set(movie.releasedate)
        self.__director.set(movie.director)
        self.__category.set(movie.category)

    def __reload_categories(self):
        """Recarga la lista de categorias con los valores que existen en el Manager de categorias"""
        self.__categories_combo.delete(0, END)

        if self.__general_manager.categories_manager:
            self.__categories_combo['values'] = self.__general_manager.categories_manager.categories

    def __reload_movies(self):
        """Recarga la lista de peliculas con los valores que existen en el Manager de peliculas"""
        self.__movies_listbox.delete(0, END)

        if self.__general_manager.movies_manager:
            movies = self.__general_manager.movies_manager.movies
            row_format = TkinterEditor.LISTBOX_ITEM_FORMAT

            for movie in movies:
                self.__movies_listbox.insert(END, row_format.format(movie.identifier, movie.title, sp=" "*2))

    def __load_content_providers(self):
        """Crea los radio buttons a mostrar en el menu de ajustes"""
        if self.__general_manager.content_providers_manager:
            providers = self.__general_manager.content_providers_manager.get_providers()
            content_provider_menu = Menu(self.__menu)

            self.__selected_content_provider = StringVar()
            self.__previous_content_provider = self.__general_manager.content_provider.key
            self.__selected_content_provider.set(self.__previous_content_provider)
            for provider in providers:
                content_provider_menu.add_radiobutton(label=provider.name, variable=self.__selected_content_provider, value=provider.key, command=self.__on_cp_menu_item_selected)

            content_provider_menu.add_separator()
            content_provider_menu.add_command(label=TkinterEditor.CONFIGURATION_MENU, command=self.__on_configuration_clicked)
            self.__menu.add_cascade(label=TkinterEditor.SETTINGS_MENU, menu=content_provider_menu)

    def __init__(self, parent: Tk = None, **configs):
        """Constructor"""
        self.__general_manager = None
        self.__selected_content_provider = None
        self.__previous_content_provider = None
        self.parent_window = parent
        self.parent_window.wm_title(TkinterEditor.APPLICATION_TITLE)
        self.parent_window.protocol('WM_DELETE_WINDOW', self.__on_exit_button_pressed)
        WindowsUtilities.center_window(self.parent_window, TkinterEditor.WINDOW_WIDTH, TkinterEditor.WINDOW_HEIGHT)

        # __main_window es la ventana principal
        self.__main_window = Frame(self.parent_window)
        self.__main_window.pack(expand=YES, fill=BOTH)

        self.__menu = Menu(self.parent_window)
        self.__settings_menu = Menu(self.__menu, tearoff=0)
        self.__settings_menu.add_command(label=TkinterEditor.EXIT_MENU, command=self.__on_exit_button_pressed) #self.parent_window.quit)
        self.__menu.add_cascade(label=TkinterEditor.SYSTEM_MENU, menu=self.__settings_menu)
        self.parent_window.config(menu=self.__menu)

        # __list_frame contiene a la lista de peliculas
        self.__list_frame = Frame(self.__main_window, height=300, width=250, borderwidth=7)
        self.__list_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        self.__scrollbar = Scrollbar(self.__list_frame, orient=VERTICAL)
        self.__movies_listbox = Listbox(self.__list_frame, yscrollcommand=self.__scrollbar.set)
        self.__scrollbar.config(command=self.__movies_listbox.yview)
        self.__scrollbar.pack(side=RIGHT, fill=Y)
        self.__movies_listbox.bind('<<ListboxSelect>>', self.__on_movies_listbox_selected)
        self.__movies_listbox.bind('<Button-3>', self.__on_movies_listbox_right_click)
        self.__movies_listbox.pack(side=LEFT, fill=BOTH, expand=YES)

        # __editor_frame contiene el editor de peliculas
        self.__editor_frame = Frame(self.__main_window, height=300, borderwidth=7)
        self.__editor_frame.pack(side=TOP, expand=NO, fill=X)

        self.__main_title_label = Label(self.__editor_frame, text=TkinterEditor.MAIN_TITLE, borderwidth=7)
        self.__main_title_label.pack(side=TOP, expand=NO, fill=X)

        # TODO: Se podria simplificar toda esta creacion
        self.__identifier_container = Frame(self.__main_window, borderwidth=7)
        self.__identifier_container.pack(side=TOP, expand=NO, fill=X)
        self.__identifier_label = Label(self.__identifier_container, text=TkinterEditor.IDENTIFIER_LABEL, borderwidth=7, width=15, anchor=W)
        self.__identifier_label.pack(side=LEFT, expand=NO)
        self.__identifier = IntVar()
        self.__identifier_text = Entry(self.__identifier_container, textvariable=self.__identifier, state='readonly')
        self.__identifier_text.pack(side=LEFT, expand=NO, fill=X)

        self.__title_container = Frame(self.__main_window, borderwidth=7)
        self.__title_container.pack(side=TOP, expand=NO, fill=X)
        self.__title_label = Label(self.__title_container, text=TkinterEditor.TITLE_LABEL, borderwidth=7, width=15, anchor=W)
        self.__title_label.pack(side=LEFT, expand=NO)
        self.__title = StringVar()
        self.__title_text = Entry(self.__title_container, textvariable=self.__title, state='readonly')
        self.__title_text.pack(side=LEFT, expand=NO, fill=X)

        self.__description_container = Frame(self.__main_window, borderwidth=7)
        self.__description_container.pack(side=TOP, expand=NO, fill=X)
        self.__description_label = Label(self.__description_container, text=TkinterEditor.DESCRIPTION_LABEL, borderwidth=7, width=15, anchor=W)
        self.__description_label.pack(side=LEFT, expand=NO)
        self.__description = StringVar()
        self.__description_text = Entry(self.__description_container, textvariable=self.__description, state='readonly')
        self.__description_text.pack(side=LEFT, expand=NO, fill=X)

        self.__releasedate_container = Frame(self.__main_window, borderwidth=7)
        self.__releasedate_container.pack(side=TOP, expand=NO, fill=X)
        self.__releasedate_label = Label(self.__releasedate_container, text=TkinterEditor.RELEASE_DATE_LABEL, borderwidth=7, width=15, anchor=W)
        self.__releasedate_label.pack(side=LEFT, expand=NO)
        self.__releasedate = StringVar()
        self.__releasedate_text = Entry(self.__releasedate_container, textvariable=self.__releasedate, state='readonly')
        self.__releasedate_text.pack(side=LEFT, expand=NO, fill=X)

        self.__director_container = Frame(self.__main_window, borderwidth=7)
        self.__director_container.pack(side=TOP, expand=NO, fill=X)
        self.__director_label = Label(self.__director_container, text=TkinterEditor.DIRECTOR_LABEL, borderwidth=7, width=15, anchor=W)
        self.__director_label.pack(side=LEFT, expand=NO)
        self.__director = StringVar()
        self.__director_text = Entry(self.__director_container, textvariable=self.__director, state='readonly')
        self.__director_text.pack(side=LEFT, expand=NO, fill=X)

        self.__category_container = Frame(self.__main_window, borderwidth=7)
        self.__category_container.pack(side=TOP, expand=NO, fill=X)
        self.__category_label = Label(self.__category_container, text=TkinterEditor.CATEGORY_LABEL, borderwidth=7, width=15, anchor=W)
        self.__category_label.pack(side=LEFT, expand=NO)
        self.__category = StringVar()
        self.__categories_combo = ttk.Combobox(self.__category_container, textvariable=self.__category, values=[], state='disabled')
        self.__categories_combo.bind('<<ComboboxSelected>>', self.__on_categories_combobox_selected)
        self.__categories_combo.pack(side=LEFT, expand=NO, fill=X)

        # __menu_frame contiene a los botones del menu
        self.__menu_frame = Frame(self.__main_window, height=50, borderwidth=7)
        self.__menu_frame.pack(side=TOP, expand=NO, fill=X)

        self.__new_button = Button(self.__menu_frame, text=TkinterEditor.ADD_BUTTON_CAPTION, command=self.__on_new_button_pressed)
        self.__new_button.pack(side=LEFT)

        self.__save_button = Button(self.__menu_frame, text=TkinterEditor.SAVE_BUTTON_CAPTION, state=DISABLED, command=self.__on_save_button_pressed)
        self.__save_button.pack(side=LEFT)

        self.__remove_button = Button(self.__menu_frame, text=TkinterEditor.REMOVE_BUTTON_CAPTION, state=DISABLED, command=self.__on_remove_movie)
        self.__remove_button.pack(side=LEFT)

        self.__exit_button = Button(self.__menu_frame, text=TkinterEditor.EXIT_BUTTON_CAPTION, command=self.__on_exit_button_pressed)
        self.__exit_button.pack(side=RIGHT)

        # Menu contextual de la lista de peliculas
        self.__movies_listbox_menu = Menu(self.__movies_listbox, tearoff=False)
        self.__movies_listbox_menu.add_command(label=TkinterEditor.EDIT_CONTEXT_MENU, command=self.__on_edit_movie)
        self.__movies_listbox_menu.add_command(label=TkinterEditor.DELETE_CONTEXT_MENU, command=self.__on_remove_movie)
        #self.__movies_listbox_menu.add_command(label=TkinterEditor.SELECT_ALL_CONTEXT_MENU, command=self.__on_not_implemented)
        self.__movies_listbox_menu.bind("<FocusOut>", lambda *args: self.__movies_listbox_menu.unpost())
