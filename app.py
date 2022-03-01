import sqlite3
import uuid

user_id = str(uuid.uuid4())
user_name = "Santiago"

##############################
db = sqlite3.connect("database.sqlite")
# question marks as place holders
db.execute("INSERT INTO users VALUES(?,?)", (user_id, user_name))
db.commit() # Write changes to the file

# Get the data from the DB
users = db.execute("SELECT * FROM users").fetchall()
print(users) 

db.execute("DELETE FROM users WHERE user_name=?", (user_name,))
# MUST commit on INSERT, UPDATE, DELETE
db.commit()














