import sqlite3
db = sqlite3.connect("database.sqlite")

user = {
  "user_id":"43cd555e-d475-4763-aeaa-788ae58f1996",
  "user_name":"NEW USER NAME"
}
try:
  # UPDATE SET WHERE
  counter = db.execute("""
    UPDATE users
    SET user_name = :user_name
    WHERE user_id = :user_id
  """, user).rowcount


  # counter = db.execute("""
  #   UPDATE users
  #   SET user_name = ?
  #   WHERE user_id = ?
  # """, ("NEW USER NAME", "43cd555e-d475-4763-aeaa-788ae58f1996")).rowcount
  db.commit()
  print(f"Number of users updated: {counter}")
except Exception as ex:
  print(ex)













