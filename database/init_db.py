from db import Database


database = Database()

with open("database/schema.sql", "r") as file:

    sql = file.read()

database.execute(sql)

database.close()

print("Database created successfully.")