import email


class MainWindowPresenter:
    def __init__(self, view, repository):
        self.view = view
        self.repository = repository

    def load_items(self):
        data = self.repository.get_all_items()
        self.view.render_table(data)




        # self.repository.add_contact(name, email)
