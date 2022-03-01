import sqlite3
import uuid

user_id = str(uuid.uuid4())
user_name = "xxx"

user = {
  "user_id" : user_id,
  "user_name" : user_name
}

db = sqlite3.connect("database.sqlite")
# Using a dictionary and named place holders
db.execute("INSERT INTO users VALUES(:user_id, :user_name)", user)


# Placeholders with ? marks
# db.execute("INSERT INTO users VALUES(?,?)",(user_id, user_name))
db.commit()


