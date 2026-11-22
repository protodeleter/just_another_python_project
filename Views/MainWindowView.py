from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QStackedWidget, QTableWidget, QTableWidgetItem,
)

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("My Application")

    def render_table(self, data):
        table = self.ui.tableWidget

        table.setColumnCount(2)
        table.setRowCount(len(data))
        table.setHorizontalHeaderLabels(["Name", "Email"])

        for row_index, record in enumerate(data):
            for col_index, value in enumerate(record):
                table.setItem(
                    row_index,
                    col_index,
                    QTableWidgetItem(str(value))
                )

