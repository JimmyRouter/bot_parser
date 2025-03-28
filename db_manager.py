import sqlite3
import constants


class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect(constants.DB_PATH)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            xpath TEXT
        )
        """)
        self.conn.commit()

    def insert_sites(self, sites):
        self.cursor.executemany(
            "INSERT INTO sites (title, url, xpath) VALUES (?, ?, ?)",
            sites
        )
        self.conn.commit()

    def get_sites(self):
        self.cursor.execute("SELECT title, url, xpath FROM sites")
        return self.cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close()

