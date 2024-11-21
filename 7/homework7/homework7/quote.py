class Quote:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, text, author_id):
        c = self.connection.cursor()
        c.execute("INSERT INTO quotes (text, author_id) VALUES (?, ?)", (text, author_id))
        self.connection.commit()

        return c.lastrowid

    def get_id_by_text(self, text):
        c = self.connection.cursor()
        c.execute("SELECT id FROM quotes WHERE text = ?", (text,))
        result = c.fetchone()
        if result is None:
            return None
        return result[0]