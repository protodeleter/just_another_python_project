from PySide6.QtWidgets import QDialog

class DialogPresenter:
    def __init__(self, view):
        self.view = view
        self.view.ui.pushButton.clicked.connect(self.on_submit)


    def on_submit(self):
        value = self.view.ui.barcodeLineEdit.text()
        print("Submitted:", value)