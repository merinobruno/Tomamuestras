import sqlite3

conn = sqlite3.connect("db.sqlite3")
with open("dump_sqlite.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()
conn.executescript(sql_script)
conn.close()