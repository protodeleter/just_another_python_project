import email


class MainWindowPresenter:
    def __init__(self, view, repository):
        self.view = view
        self.repository = repository
        self.view.item_clicked.connect(self.on_item_clicked)

    def load_items(self):
        data = self.repository.get_all_items()
        self.view.render_table(data)

    def on_item_clicked(self, item_id):
        self.repository.delete_item(item_id)
        self.load_items()

        # self.repository.add_contact(name, email)
