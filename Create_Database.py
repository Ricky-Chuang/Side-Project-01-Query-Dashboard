import sqlite3
import pandas as pd

supermarket_dataset = pd.read_excel('supermarket_dataset.xlsx')

connection = sqlite3.connect('supermarket_dataset.db')  #建立資料庫
cursor = connection.cursor()
create_table = '''
CREATE TABLE supermarket_dataset(
    Invoice_ID STRING NOT NULL, 
    Customer_type STRING NOT NULL, 
    Gender STRING NOT NULL, 
    Product_line STRING NOT NULL, 
    Unit_price INTEGER,
    Quantity INTEGER, 
    Tax_5_percent INTEGER, 
    Total INTEGER, 
    Date DATE NOT NULL, 
    Time DATETIME NOT NULL, 
    Payment INTEGER, 
    Branch STRING NOT NULL,
    City STRING NOT NULL, 
    Rating INTEGER)
    ;
'''
cursor.execute(create_table)  #建立資料表
connection.commit()
connection.close()


#如果資料表存在，就寫入資料，否則建立資料表
connection = sqlite3.connect('supermarket_dataset.db')
supermarket_dataset.to_sql('supermarket_dataset', connection, if_exists='append', index=False)
connection.commit()
connection.close()