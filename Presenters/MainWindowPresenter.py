
from Views.DialogView import DialogView

class MainWindowPresenter:
    def __init__(self, view, repository):
        self.view = view
        self.repository = repository
        self.view.item_clicked.connect(self.on_item_clicked)
        self.view.ui.pushButton.clicked.connect(self.on_click)


    def load_items(self):
        data = self.repository.get_all_items()
        self.view.render_table(data)


    def on_item_clicked(self, item_id):
        self.repository.delete_item(item_id)
        self.load_items()

    def on_click(self):
        dialog = DialogView(self.view)
        dialog.exec()

    def show_popup(self):
        pass

        # self.repository.add_contact(name, email)
