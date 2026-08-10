import sqlite3
DB="nexra_research.db"
def connect(): return sqlite3.connect(DB)
def save(session,text,score): return True
def start(domain,q): return connect().execute("INSERT INTO research_sessions(domain,query) VALUES(?,?)",(domain,q)).lastrowid
def finding(s,u,t,score): connect().execute("INSERT INTO research_findings(session_id,source_url,raw_text,trust_score) VALUES(?,?,?,?)",(s,u,t,score))
