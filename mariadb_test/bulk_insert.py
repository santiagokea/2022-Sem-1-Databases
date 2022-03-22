import mysql.connector

db_config = {
  "host":"localhost",
  "port": 3306,
  "user":"root",
  "password":"",
  "database":"twitter"
}

db_conn = mysql.connector.connect(**db_config)
db = db_conn.cursor()

sql = "INSERT INTO users (user_name, user_email) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652')
]
db.executemany(sql, val)
counter = db.rowcount
db_conn.commit()

