import sqlite3
db = sqlite3.connect("database.sqlite")
# UPDATE SET WHERE
counter = db.execute("""
  UPDATE users
  SET user_name = ?
  WHERE user_id = ?
""", ("NEW USER NAME", "43cd555e-d475-4763-aeaa-788ae58f1996")).rowcount
db.commit()
print(f"Number of users updated: {counter}")













