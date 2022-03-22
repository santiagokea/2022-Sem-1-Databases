import mysql.connector
import json

db_config = {
  "host":"localhost",
  "port": 3306,
  "user":"root",
  "password":"",
  "database":"twitter"
}

#db.sqlite3.connect
db_conn = mysql.connector.connect(**db_config)
# Without dictionary = True it returns a multi-dimensional array
# [[1, "a", "@a"], [2, "b", "@b"]]
db = db_conn.cursor(dictionary=True)
# print("*****")
print(dir(db))

db.execute("SELECT * FROM users")
users = db.fetchall()
print(json.dumps(users))
