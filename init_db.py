import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (id, title, content) VALUES (?, ?, ?)", 
            ('1', 'First', 'Neil'))

cur.execute("INSERT INTO posts (id, title, content) VALUES (?, ?, ?)",
            ('2', 'Second Post', 'Buzz Aldrin'))

connection.commit()
connection.close()