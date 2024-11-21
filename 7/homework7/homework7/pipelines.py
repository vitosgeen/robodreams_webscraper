# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from homework7 import setup_database
from homework7 import author
from homework7 import quote
from homework7 import tag


class Homework7Pipeline:
    def open_spider(self, spider):
        self.file = open("quotes.json", "w")
        setup_database.setup_database()
        self.connection = sqlite3.connect(setup_database.database_name)
        self.cursor = self.connection.cursor()
        self.author = author.Author(self.connection)
        self.quote = quote.Quote(self.connection)
        self.tag = tag.Tag(self.connection)

    def close_spider(self, spider):
        self.file.close()
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        # add the author to the database
        author_name = item["author"]
        # check if the author is already in the database
        author_id = self.author.get_id_by_name(author_name)
        if author_id is None:
            author_id = self.author.insert(author_name)

        # add the quote to the database
        quote_text = item["text"]
        # check if the quote is already in the database
        quote_id = self.quote.get_id_by_text(quote_text)
        if quote_id is None:
            quote_id = self.quote.insert(quote_text, author_id)

        # add the tags to the database
        tags = item["tags"]
        for tag in tags:
            tag_id = self.tag.get_id_by_name(tag)
            if tag_id is None:
                tag_id = self.tag.insert(tag)

            # check if the quote-tag relationship is already in the database
            quote_tag = self.tag.get_id_by_quote_id_tag_id(quote_id, tag_id)
            if quote_tag is None:
                self.tag.insert_quote_tag(quote_id, tag_id)

        # write the item to the file
        self.file.write(f"{item}\n")
        
        return item
