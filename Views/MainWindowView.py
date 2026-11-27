from logging import log

from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QTableWidgetItem, QDialog,
)
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    item_clicked = Signal(int)  # Define a signal carrying an integer

    def __init__(self):
        super().__init__()
        self.button = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("My Application")

    def render_table(self, data):
        table = self.ui.tableWidget
        table.setColumnCount(5)
        table.setRowCount(len(data))
        table.setHorizontalHeaderLabels(["Title", "Barcode", "Created", "Updated", "Action"])
        for row_index, record in enumerate(data):
            for col_index, value in enumerate(record):
                if col_index == 4:
                    self.button = QPushButton("Click Me", self)
                    table.setCellWidget(row_index, col_index , self.button)
                    self.button.clicked.connect(
                        lambda checked=False, item_id=record[0]:
                        self.item_clicked.emit(item_id)
                    )
                else:
                    table.setItem(
                        row_index,
                        col_index,
                        QTableWidgetItem(str(value))
                    )
