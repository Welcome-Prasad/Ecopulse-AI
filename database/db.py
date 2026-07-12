import sqlite3
import os


class Database:

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        self.connection = sqlite3.connect(
            "database/eco.db"
        )

        self.cursor = self.connection.cursor()

    def execute(self, query, values=None):

        if values:

            self.cursor.execute(query, values)

        else:

            self.cursor.execute(query)

        self.connection.commit()

    def fetchall(self):

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()