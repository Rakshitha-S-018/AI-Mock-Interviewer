import sqlite3

connection = sqlite3.connect("data/users.db")

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS interviews(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

role TEXT,

score INTEGER

)

""")

connection.commit()

connection.close()