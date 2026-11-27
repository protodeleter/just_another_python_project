from PySide6.QtWidgets import QDialog
from Repositories.ItemRepository import ItemRepository
class DialogPresenter:
    def __init__(self, view, repository):
        self.view = view
        self.view.ui.pushButton.clicked.connect(self.on_submit)
        self.repository = repository


    def on_submit(self):
        value = self.view.ui.barcodeLineEdit.text()

        self.repository.add_item(value)

        print("Submitted:", value)