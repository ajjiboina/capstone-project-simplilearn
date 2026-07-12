# imports
import sqlite3
# Connect to Product DB
connection = sqlite3.connect("db/products.db")
# Run the Query 
cursor = connection.cursor()
cursor.execute("SELECT * FROM products")
# Fetch the db Rows
db_rows = cursor.fetchall()
for row in db_rows:
    print(row)

# Close the Connection
connection.close()