from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIntValidator

from Views.MainWindowView import MainWindow
from dialog import Ui_Dialog

class DialogView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.barcodeLineEdit.setValidator(
            QIntValidator(1, 999999999, self)
        )

