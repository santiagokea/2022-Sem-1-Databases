import sqlite3

user = {
  "user_name":"a"
}

db = sqlite3.connect("database.sqlite")
# db.execute("DELETE FROM users WHERE user_name = ?", ("xxx",))
counter = db.execute("DELETE FROM users WHERE user_name = :user_name", user).rowcount
db.commit()
print(f"Number of users deleted: {counter}")
