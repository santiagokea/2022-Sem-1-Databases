import sqlite3

user = {
  "user_name":"a"
}
try:
  db = sqlite3.connect("database.sqlite")
  # db.execute("DELETE FROM users WHERE user_name = ?", ("xxx",))
  counter = db.execute("DELETEx FROM users WHERE user_name = :user_name", user).rowcount
  if not counter: print("Nothing was deleted")
  db.commit()
  print(f"Number of users deleted: {counter}")
except Exception as ex:
  print(ex)