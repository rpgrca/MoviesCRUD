"""moviesCRUD.py"""

from tkinter import Tk
from Editor.TkinterEditor import TkinterEditor
from Manager.GeneralManager import GeneralManager

if __name__ == '__main__':
    ROOT = Tk()
    EDITOR = TkinterEditor(ROOT)

    MANAGER = GeneralManager()
    MANAGER.select_content_provider('memory')
    MANAGER.load()

    EDITOR.set_general_manager(MANAGER)
    ROOT.mainloop()

    MANAGER.dump()
    MANAGER.save()
