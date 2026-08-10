import sqlite3
DB="nexra_research.db"
def connect(): return sqlite3.connect(DB)
def save(session,text,score): return True
def start(domain,q): return connect().execute("INSERT INTO research_sessions(domain,query) VALUES(?,?)",(domain,q)).lastrowid
