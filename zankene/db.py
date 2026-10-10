import sqlite3
import logging

class ZankeneDatabase:
    def __init__(self, db_name="zankene_v10.db"):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS task_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id INTEGER,
                    task_name TEXT,
                    status TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
        logging.info(f"💾 [ZANKENE DB] SQLite Database '{self.db_name}' Initialized.")

    def log_task(self, task_id, task_name, status):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO task_logs (task_id, task_name, status) VALUES (?, ?, ?)",
                (task_id, task_name, status)
            )
            conn.commit()
        logging.info(f"📝 [DB LOGGED] Task #{task_id} status saved as '{status}'")

    def fetch_all_logs(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, task_id, task_name, status, timestamp FROM task_logs ORDER BY id DESC")
            rows = cursor.fetchall()
            return rows