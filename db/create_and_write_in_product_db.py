#imports
import sqlite3


#2 Write the data that we want to push to our created DB
PRODCUT_DB = {
    "iphone 17 pro max": {
        "brand": "Apple",
        "price": 999.99,
        "stock": 100
    },
    "Samsung Galaxy S26 Ultra": {
        "brand": "Samsung",
        "price": 1299.99,
        "stock": 50
    },
    # Add more products as needed
}
# Create connection to SQLite database
connection=sqlite3.connect("db/products.db")
# Create a cursor object to execute SQL commands
cursor=connection.cursor()
# Create a table to store product information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand TEXT,
        price REAL,
        stock INTEGER
    )
'''
)
for product_name, details in PRODCUT_DB.items():
    cursor.execute('''
        INSERT INTO products (name, brand, price, stock)
        VALUES (?, ?, ?, ?)
    ''', (product_name, details["brand"], details["price"], details["stock"]))

# Commit Changes
connection.commit()
# Close the connection
connection.close()

print("Product database created and data inserted successfully.")
