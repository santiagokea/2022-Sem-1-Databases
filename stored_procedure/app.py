# import mysql.connector
# import mariadb
import pymysql

try:
  db_config = {
  "host":"localhost",
  "port": 3306,
  "user":"root",
  "password":"",
  "database":"company_29_march"
}
  # db_conn = mysql.connector.connect(**db_config)
  # db_conn = mariadb.connect(**db_config)
  db_conn = pymysql.connect(**db_config)
  print(dir(db_conn))
  db = db_conn.cursor()
  db.execute("CALL get_users()")
  users = db.fetchall()
  print(users)
except Exception as ex:
  print(ex)
finally:
  print("finally")