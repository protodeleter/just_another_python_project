from Services import database

class ItemRepository:

    def __init__(self, connection_factory):
        self.connection_factory = connection_factory

    def get_item(self, item_id):
        pass



    def delete_item(self, item_id):
        pass

    def update_item(self, item_id, item_data):
        pass

    def get_all_items(self):

        with self.connection_factory() as conn:
            cur = conn.cursor()
            data = cur.execute("SELECT * FROM items")
            res = data.fetchall()
        cur.close()
        conn.close()

        return res


    def insert_item(self, item_data):
        pass

