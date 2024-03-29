"""SettingsEditor.py"""

#from tkinter import *
from tkinter import Label, Frame, Entry, StringVar, Tk, Button
from tkinter import TOP, YES, NO, X, W, LEFT, BOTH, CENTER
from Manager.ContentProvider.ContentProvidersManager import ContentProvidersManager
from Manager.ContentProvider import ContentProvider
from Editor.WindowsUtilities import WindowsUtilities

class SettingsEditor(object):
    """Interface grafica del editor de configuracion"""
    WINDOW_TITLE = "Editor de Configuracion"
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    SAVE_BUTTON_CAPTION = "Grabar"
    CANCEL_BUTTON_CAPTION = "Cancelar"

    def configure(self, content_providers_manager: ContentProvidersManager, current_content_provider: ContentProvider):
        """Carga el manejador de Content Providers y crea los controles para configurar cada uno"""
        self.__content_providers_manager = content_providers_manager

        for content_provider in content_providers_manager.get_providers():
            frame = Frame(self.__main_frame, borderwidth=7)
            frame.pack(side=TOP, expand=NO, fill=X)
            label = Label(frame, text=content_provider.name, borderwidth=7, width=15, anchor=W)
            label.pack(side=LEFT, expand=NO)

            if content_provider.extra_data is None:
                text = Entry(frame, width=45, state='readonly')
                text.pack(side=LEFT, expand=NO, fill=X)
            else:
                if not isinstance(content_provider.extra_data, list):
                    extra_datas = [content_provider.extra_data]
                else:
                    extra_datas = content_provider.extra_data

                state = 'readonly' if content_provider.key == current_content_provider.key else 'normal'
                self.__variables[content_provider.key] = {'variable': [], 'label': label}
                for extra_data in extra_datas:
                    variable = StringVar()
                    variable.set(extra_data)
                    self.__variables[content_provider.key]['variable'].append(variable)
                    text = Entry(frame, textvariable=variable, width=int(45 / len(extra_datas)), state=state)
                    text.pack(side=LEFT, expand=NO, fill=X)

    def __on_exit_button_pressed(self):
        """Callback llamada al querer salir de la ventana"""
        self.parent_window.destroy()

    def __on_save_button_pressed(self):
        """Callback llamada al editar cada configuracion"""
        can_save = True
        for key in self.__variables.keys():
            color = 'black'
            strings = []

            for variable in self.__variables[key]['variable']:
                # Si algun campo esta vacio, error
                strings.append(variable.get())
                if not variable.get():
                    color = 'red'
                    break

            if color != 'red':
                if len(set(strings)) != len(self.__variables[key]['variable']):
                    # Si algun campo esta duplicado, error
                    color = 'red'

            self.__variables[key]['label']['fg'] = color
            if color == 'red':
                can_save = False

        if can_save:
            for content_provider in self.__content_providers_manager.get_providers():
                if content_provider.key in self.__variables:
                    if len(self.__variables[content_provider.key]['variable']) == 1:
                        new_extra_data = self.__variables[content_provider.key]['variable'][0].get()
                        if content_provider.extra_data != new_extra_data:
                            content_provider.refresh(new_extra_data)
                    else:
                        new_extra_data = list(map(lambda x: x.get(), self.__variables[content_provider.key]['variable']))
                        if content_provider.extra_data != new_extra_data:
                            content_provider.refresh(new_extra_data)

        self.parent_window.destroy()

    def __on_cancel_button_pressed(self):
        """Callback llamada al presionar el boton Cancel: se descartan todos los cambios"""
        # TODO: Si hay cambios deberia preguntar si desea perderlos
        self.parent_window.destroy()

    def __init__(self, parent: Tk = None, **_configs):
        """Constructor"""
        self.__content_providers_manager = None
        self.__variables = {}
        self.parent_window = parent
        self.parent_window.resizable(False, False)
        self.parent_window.wm_title(SettingsEditor.WINDOW_TITLE)
        self.parent_window.protocol("WM_DELETE_WINDOW", self.__on_exit_button_pressed)
        self.parent_window.geometry("{}x{}".format(SettingsEditor.WINDOW_WIDTH, SettingsEditor.WINDOW_HEIGHT))

        # __main_window es la ventana principal
        self.__main_window = Frame(self.parent_window)
        self.__main_window.pack(expand=YES, fill=BOTH)

        self.__main_frame = Frame(self.__main_window)
        self.__main_frame.pack(expand=YES, fill=BOTH)

        self.__button_frame = Frame(self.__main_window, padx=10)
        self.__button_frame.pack(expand=YES, fill=BOTH)

        self.__button_save = Button(self.__button_frame,
                                    text=SettingsEditor.SAVE_BUTTON_CAPTION,
                                    command=self.__on_save_button_pressed, padx=5)
        self.__button_save.place(relx=0.43, rely=0.5, anchor=CENTER)

        self.__button_cancel = Button(self.__button_frame,
                                      text=SettingsEditor.CANCEL_BUTTON_CAPTION,
                                      command=self.__on_cancel_button_pressed, padx=5)
        self.__button_cancel.place(relx=0.57, rely=0.5, anchor=CENTER)

        WindowsUtilities.center_window(self.parent_window, SettingsEditor.WINDOW_WIDTH, SettingsEditor.WINDOW_HEIGHT)
