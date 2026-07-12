#imports
#Make the SQLLite database and create the tables,Commit Changes, and close the connection
import sqlite3
connection=sqlite3.connect('db/memory.db')

cursor=connection.cursor()

cursor.execute(""""
               CREATE TABLE IF NOT EXISTS conversation_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                session_id TEXT, 
                role TEXT, 
                message TEXT, 
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)) 
               """)

connection.commit()
connection.close()

