"""SettingsEditor.py"""

from tkinter import *
from Manager.ContentProvider.ContentProvidersManager import ContentProvidersManager
from Editor.WindowsUtilities import WindowsUtilities

class SettingsEditor(object):
    WINDOW_TITLE = "Editor de Configuracion"
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    def configure(self, content_providers_manager: ContentProvidersManager):
        """Carga el Manager de Content Providers"""
        self.__content_providers_manager = content_providers_manager

        for content_provider in content_providers_manager.get_providers():
            frame = Frame(self.__main_window, borderwidth=7)
            frame.pack(side=TOP, expand=NO, fill=X)
            label = Label(frame, text=content_provider.name, borderwidth=7, width=15, anchor=W)
            label.pack(side=LEFT, expand=NO)

            variable = StringVar()
            if content_provider.extra_data is None:
                variable.set("")
                state = 'readonly'
            else:
                variable.set(content_provider.extra_data)
                state = 'normal'
                self.__variables[content_provider.key] = { 'variable': variable, 'label': label }

            text = Entry(frame, textvariable=variable, validate='focusout', validatecommand=self.__on_entry_validation, width=45, state=state)
            text.pack(side=LEFT, expand=NO, fill=X)

    def __on_exit_button_pressed(self):
        """Callback llamado al querer salir de la ventana"""
        self.parent_window.destroy()

    def __on_entry_validation(self):
        """Callback llamada al editar cada configuracion"""
        for key in self.__variables.keys():
            self.__variables[key]['label']['fg'] = 'black' if self.__variables[key]['variable'].get() else 'red'

    def __init__(self, parent: Tk = None, **configs):
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

        WindowsUtilities.center_window(self.parent_window, SettingsEditor.WINDOW_WIDTH, SettingsEditor.WINDOW_HEIGHT)
