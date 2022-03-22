from faker import Faker
fake = Faker()
import uuid
import sqlite3 
import time

# print(fake.name()) # Dylan Garcia
# print(fake.first_name()) # Ronald
# print(fake.email()) # nancygarner@example.org

# users = []
# for _ in range(1000):
#   user = {
#     "user_id" : str(uuid.uuid4()),
#     "user_name" : fake.first_name(),
#     "user_email" : fake.email()
#   }
#   users.append(user)

while True:
  # List comprehension
  users = [  {
      "user_id" : str(uuid.uuid4()),
      "user_name" : fake.first_name(),
      "user_email" : str(uuid.uuid4()) + fake.email(),
      "user_password" : fake.password(),
    } for _ in range(10000)  ]


  try:
    db = sqlite3.connect("data.db")
    counter = db.executemany("""
      INSERT INTO users 
      VALUES(:user_id, :user_name, :user_email, :user_password)""", users).rowcount
    db.commit()
    if not counter: print("uppps...") 
    print(f"Rows added: {counter}")
  except Exception as ex:
    print(ex)  
  finally:
    db.close()

  time.sleep(5)



