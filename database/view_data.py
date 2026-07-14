from database.db import Database

db = Database()

rows = db.get_all_logs()

for row in rows:
    print(row)

db.close()