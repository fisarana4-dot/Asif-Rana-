import sqlite3
DB="nexra_research.db"
def connect(): return sqlite3.connect(DB)
