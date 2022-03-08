import sqlite3

db = sqlite3.connect("database.sqlite")

user_id = "1"
user_name = "m"
user_email = None

new_item = {"user_id":user_id}
set_parts = []

if user_name:
  set_parts.append("user_name=:user_name")
  new_item["user_name"] = user_name

print(set_parts)
print(new_item)

