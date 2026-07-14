from db import Database

db = Database()

db.create_tables()

db.close()

print("Database initialized successfully.")