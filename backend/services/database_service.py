import sqlite3


class DatabaseService:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/eco.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

    def get_all_logs(self):

        self.cursor.execute("""
            SELECT *
            FROM machine_logs
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def get_latest_logs(self):

        self.cursor.execute("""
            SELECT *
            FROM machine_logs
            WHERE id IN (
                SELECT MAX(id)
                FROM machine_logs
                GROUP BY machine_id
            )
            ORDER BY machine_id
        """)

        return self.cursor.fetchall()