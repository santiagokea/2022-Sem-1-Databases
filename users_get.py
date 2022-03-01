import sqlite3
import json

db = sqlite3.connect("database.sqlite")
users = json.dumps(db.execute("SELECT * FROM users").fetchall())
print(users)



