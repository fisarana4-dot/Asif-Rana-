
import sqlite3
DB="nexra_evidence.db"

def save_evidence(h):
 c=sqlite3.connect(DB)
 c.execute("CREATE TABLE IF NOT EXISTS evidence(id INTEGER PRIMARY KEY,hash TEXT)")
 c.execute("INSERT INTO evidence
