import mysql.connector
from itemadapter import ItemAdapter
import sqlite3

class SipwhiskeyPipeline:
    def __init__(self):
        #self.con = sqlite3.connect('mydatabase')

        self.con = mysql.connector.connect(
            host = '34.132.53.100',
            user ="byron",
            database = 'database',
            password = '******',
        )
        
        self.cur = self.con.cursor()
        self.create_table()
        
    def create_table(self):
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS products(
            id INT  AUTO_INCREMENT PRIMARY KEY ,
            name TEXT,
            brand TEXT,
            price DOUBLE
            )""")
        

    
    def process_item(self, item, spider):
        self.cur.execute(""" INSERT INTO products (name , brand ,price) VALUES (%s, %s , %s) """ , (item['name'], item['brand'] , item['price']))
        #""" insert into quotes (content, tags, author) values (%s,%s,%s)"""
        self.con.commit()
        return item
    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
