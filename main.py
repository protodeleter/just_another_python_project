import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

from Services import database

try:
    with database.get_connection() as conn:
        result = conn.execute(
            "SELECT current_database(), current_user"
        ).fetchone()

        print("Connected successfully!")
        print("Database:", result[0])
        print("User:", result[1])

except Exception as error:
    print("Connection failed:", error)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(
            self.save_contact
        )

    def save_contact(self):


        name = self.ui.plainTextEdit.toPlainText()
        email = self.ui.plainTextEdit_2.toPlainText()

        print(f"Saving: {name}, {email}")

        # Later, insert into PostgreSQL here


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())