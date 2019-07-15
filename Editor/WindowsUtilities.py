from tkinter import *

class WindowsUtilities:
    @staticmethod
    def center_window(win: Tk, window_width: int, window_height: int):
        """Centra la ventana dada en la pantalla"""
        x_cordinate = int((win.winfo_screenwidth() - window_width) / 2)
        y_cordinate = int((win.winfo_screenheight() - window_height) / 2)

        win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
