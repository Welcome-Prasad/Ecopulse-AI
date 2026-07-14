import sqlite3
import os


class Database:

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        self.connection = sqlite3.connect("database/eco.db")

        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS machine_logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            machine_id TEXT,

            machine_name TEXT,

            voltage REAL,

            current REAL,

            power REAL,

            temperature REAL,

            efficiency REAL,

            health REAL,

            runtime INTEGER
        )
        """)

        self.connection.commit()

    def insert_machine(self, timestamp, machine):

        self.cursor.execute("""

        INSERT INTO machine_logs(

            timestamp,
            machine_id,
            machine_name,
            voltage,
            current,
            power,
            temperature,
            efficiency,
            health,
            runtime

        )

        VALUES(?,?,?,?,?,?,?,?,?,?)

        """, (

            timestamp,
            machine.machine_id,
            machine.name,
            machine.voltage,
            machine.current,
            machine.power,
            machine.temperature,
            machine.efficiency,
            machine.health,
            machine.runtime

        ))

        self.connection.commit()

    def get_all_logs(self):

        self.cursor.execute("SELECT * FROM machine_logs")

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()