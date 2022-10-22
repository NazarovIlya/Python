import sqlite3


d_base = sqlite3.connect("personal.db")

curs = d_base.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS personal(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first name TEXT,
    family TEXT,
    position TEXT,
    salary INT,
    bonus INT
    )''')