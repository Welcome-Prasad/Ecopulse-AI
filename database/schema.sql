CREATE TABLE IF NOT EXISTS machine_logs (

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

);