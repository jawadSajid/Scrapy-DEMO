# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# Scraped data -> Item Containers -> Json/Csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo  DB

import sqlite3


class QuotesPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                 title text,
                 author text,
                 tag text
                 )""")

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values(
                            ?, ? , ?)""", (item['title'][0],
                                           item['author'][0],
                                           item['tag'][0]))

        self.conn.commit()

    def process_item(self, item, spider):
        # print("pipeline:" + item['title'][0])
        self.store_db(item)
        return item
