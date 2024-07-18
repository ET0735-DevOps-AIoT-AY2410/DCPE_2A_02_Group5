import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table for users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, barcode TEXT)''')

# Insert some example data
c.execute("INSERT INTO users (name, barcode) VALUES (?, ?)", ("Alice", "123456789"))
c.execute("INSERT INTO users (name, barcode) VALUES (?, ?)", ("Bob", "987654321"))

# Commit and close the database connection
conn.commit()
conn.close()