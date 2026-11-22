import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from Presenters.MainWindowPresenter import MainWindowPresenter
from Repositories.ItemRepository import ItemRepository
from Services import database
from Services.database import get_connection
from Views.MainWindowView import MainWindow


try:
    with database.get_connection() as conn:
        result = conn.execute(
            "SELECT table_schema, table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema') ORDER BY table_schema, table_name" ).fetchone()

        print("Connected successfully!")
        print("Database:", result[0])
        print("User:", result[1])

except Exception as error:
    print("Connection failed:", error)





def main():
    app = QApplication(sys.argv)

    main_view = MainWindow()

    repository = ItemRepository(get_connection)

    presenter = MainWindowPresenter(main_view, repository)

    presenter.load_items()

    main_view.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())


# main window -> table items stored already
# --> item name | item code | quantity | button(remove) | button (update)

# button -> add item
# --> opens interface to add item ( field to paste barcode | quantity (if barcode is correct ) ) | item name | button add item
#
# search field (filters table for results )
