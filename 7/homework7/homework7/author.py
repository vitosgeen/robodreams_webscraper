class Author:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, name):
        c = self.connection.cursor()
        c.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        self.connection.commit()

        return c.lastrowid

    def get_id_by_name(self, name):
        c = self.connection.cursor()
        c.execute("SELECT id FROM authors WHERE name = ?", (name,))
        result = c.fetchone()
        if result is None:
            return None
        return result[0]