"""SettingsEditor.py"""

from tkinter import Tk

class SettingsEditor:
    WINDOW_TITLE = "Editor de Configuracion"
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    def __on_exit_button_pressed(self):
        pass

    def __init__(self, parent: Tk = None, **configs):
        """Constructor"""
        self.__general_manager = None
        self.__selected_content_provider = "empty"
        self.parent_window = parent
        self.parent_window.wm_title(SettingsEditor.WINDOW_TITLE)
        self.parent_window.protocol("WM_DELETE_WINDOW", self.__on_exit_button_pressed)
        self.parent_window.geometry("{}x{}".format(SettingsEditor.WINDOW_WIDTH, SettingsEditor.WINDOW_HEIGHT))

        # __main_window es la ventana principal
        self.__main_window = Frame(self.parent_window)
        self.__main_window.pack(expand=YES, fill=BOTH)

