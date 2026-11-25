from PySide6.QtWidgets import QDialog

from Views.MainWindowView import MainWindow
from dialog import Ui_Dialog

class DialogView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)