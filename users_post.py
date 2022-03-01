import sqlite3
import uuid

user_id = str(uuid.uuid4())
user_name = "b"
user_email = "@a"

user = {
  "user_id" : user_id,
  "user_name" : user_name,
  "user_email" : user_email
}

try:
  db = sqlite3.connect("database.sqlite")
  # Using a dictionary and named place holders
  db.execute("INSERT INTO users VALUES(:user_id, :user_name, :user_email)", user)
  # Placeholders with ? marks
  # db.execute("INSERT INTO users VALUES(?,?)",(user_id, user_name))
  db.commit()
except Exception as ex:
  print(type(ex))
  if "user_email" in str(ex): 
    print("Email already exists")

