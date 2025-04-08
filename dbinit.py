import sqlite3
from config import settings

def init_db():
    with sqlite3.connect(settings.DB_FILE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            resume_path TEXT NOT NULL,
            state TEXT NOT NULL DEFAULT 'PENDING'
        )''')

init_db()
