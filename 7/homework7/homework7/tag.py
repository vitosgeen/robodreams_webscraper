class Tag:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def insert(self, name):
        self.cursor.execute("INSERT INTO tags (name) VALUES (?)", (name,))
        self.conn.commit()

        return self.cursor.lastrowid

    def get_id_by_name(self, name):
        self.cursor.execute("SELECT id FROM tags WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        if result is None:
            return None
        return result[0]
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM tags")
        return self.cursor.fetchall()
    
    def get_by_quote_id(self, quote_id):
        self.cursor.execute("SELECT tags.name FROM tags JOIN quotes_tags ON tags.id = quotes_tags.tag_id WHERE quotes_tags.quote_id = ?", (quote_id,))
        return self.cursor.fetchall()
    
    def insert_quote_tag(self, quote_id, tag_id):
        self.cursor.execute("INSERT INTO quotes_tags (quote_id, tag_id) VALUES (?, ?)", (quote_id, tag_id))
        self.conn.commit()

    def get_id_by_quote_id(self, quote_id):
        self.cursor.execute("SELECT tag_id FROM quotes_tags WHERE quote_id = ?", (quote_id,))
        return self.cursor.fetchall()
    
    def get_quote_id_by_tag_id(self, tag_id):
        self.cursor.execute("SELECT quote_id FROM quotes_tags WHERE tag_id = ?", (tag_id,))
        return self.cursor.fetchall()
    
    def get_id_by_quote_id_tag_id(self, quote_id, tag_id):
        self.cursor.execute("SELECT * FROM quotes_tags WHERE quote_id = ? AND tag_id = ?", (quote_id, tag_id))
        return self.cursor.fetchone()